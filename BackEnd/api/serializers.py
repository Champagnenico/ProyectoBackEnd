from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Game, SquadRequest


class RegisterSerializer(serializers.ModelSerializer):
    gamertag = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'gamertag']

    def create(self, validated_data):
        gamertag = validated_data.pop('gamertag')
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        Profile.objects.create(user=user, gamertag=gamertag)
        return user


class UserSerializer(serializers.ModelSerializer):
    gamertag = serializers.CharField(source='profile.gamertag')

    class Meta:
        model = User
        fields = ['username', 'gamertag']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class SquadRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    game = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Game.objects.all()
    )

    class Meta:
        model = SquadRequest
        fields = "__all__"

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("La descripción debe tener al menos 10 caracteres")
        return value
