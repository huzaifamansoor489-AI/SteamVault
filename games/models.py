from django.db import models

class Game(models.Model):
    game_name = models.CharField(max_length=100)
    game_genre = models.CharField(max_length=100)
    game_platform = models.CharField(max_length=100)
    game_developer = models.CharField(max_length=100)
    release_year = models.IntegerField()
    hours_played = models.IntegerField()
    game_description = models.CharField(max_length=500)
    status = models.CharField(max_length=100)
    rating = models.IntegerField()
    