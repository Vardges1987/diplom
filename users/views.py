from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
from django.db import IntegrityError
from game.models import Level
from .models import UserProfile
from users.forms import UserEditProfileForm
from django.contrib import messages
from .models import UserProgress
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer


class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@login_required
def profile(request):
    user_progress, created = UserProgress.objects.get_or_create(user=request.user, defaults={'level_id': 1})

    if not Level.objects.filter(id=user_progress.level_id).exists():
        user_progress.level_id = 1
        user_progress.save()

    current_level = get_object_or_404(Level, id=user_progress.level_id)
    puzzle_url = reverse('game:puzzle_view', kwargs={'level_id': user_progress.level_id})

    if request.method == "POST":
        next_level = user_progress.level_id + 1
        if Level.objects.filter(id=next_level).exists():
            user_progress.level_id = next_level
            user_progress.save()
        return redirect('profile')

    return render(request, 'users/profile.html', {
        'level_id': user_progress.level_id,
        'puzzle_url': puzzle_url,
        'current_level': current_level,
    })


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'registration/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return render(request, 'registration/register.html')

        try:
            user = User.objects.create_user(username=username, password=password)
            UserProfile.objects.create(user=user)  # Create user profile
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
        except IntegrityError:
            messages.error(request, 'Error creating user. Try a different username.')
            return render(request, 'registration/register.html')

    return render(request, 'registration/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if not hasattr(user, 'userprofile'):
                messages.error(request, 'User profile does not exist.')
                return redirect('edit_profile')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'registration/login.html', {'username': username})

    return render(request, 'registration/login.html')


def logout(request):
    auth_logout(request)
    return redirect('home')


@login_required
def edit_profile(request):
    user = request.user

    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UserEditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users/profile')
    else:
        form = UserEditProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form})


def home(request):
    return render(request, 'home.html')
