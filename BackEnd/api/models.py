from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gamertag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.gamertag


class Game(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    cover_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class SquadRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rank_required = models.CharField(max_length=50)
    mic_required = models.BooleanField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
