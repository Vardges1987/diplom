from rest_framework import generics
from .models import Game
from django.contrib.auth.models import User
from .serializers import UserSerializer, GameSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
