from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Game, Level


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class GameSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Game
        fields = ['user', 'level', 'score', 'created_at']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'