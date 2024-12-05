from rest_framework import generics
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
