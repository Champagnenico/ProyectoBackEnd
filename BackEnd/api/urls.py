from django.urls import path
from .views import RegisterView, GameList, SquadListCreate, SquadDelete

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('games/', GameList.as_view()),
    path('squads/', SquadListCreate.as_view()),
    path('squads/<int:pk>/', SquadDelete.as_view()),
]
