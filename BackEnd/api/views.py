from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Game, SquadRequest
from .serializers import (
    RegisterSerializer,
    GameSerializer,
    SquadRequestSerializer
)
from .permissions import IsOwner




class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer




class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer




class SquadListCreate(generics.ListCreateAPIView):
    serializer_class = SquadRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = SquadRequest.objects.all().order_by('-created_at')
        game_slug = self.request.query_params.get('game_slug')
        if game_slug:
            queryset = queryset.filter(game__slug=game_slug)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SquadDelete(generics.DestroyAPIView):
    queryset = SquadRequest.objects.all()
    serializer_class = SquadRequestSerializer
    permission_classes = [IsAuthenticated, IsOwner]
