from django.db import models
from movshare.users.models import User

# Create your models here.

class Shelf(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User, related_name='shelves', blank=True, null=True,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.name

class Media(models.Model):
    name = models.CharField(max_length=255)
    MOVIE_TYPE = "movie"
    GAME_TYPE = "game"
    MUSIC_TYPE = "music"
    OTHER_TYPE = "other"

    MEDIA_TYPE = (
        (MOVIE_TYPE, "Movie"),
        (GAME_TYPE, "Game"),
        (MUSIC_TYPE, "Music"),
        (OTHER_TYPE, "Other"),
    )

    media_type = models.CharField(max_length=255, choices=MEDIA_TYPE)
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey(
        User, related_name='Media', blank=True, null=True,
        on_delete=models.CASCADE,
        )
    shelf = models.ForeignKey(
        Shelf, related_name='Media', blank=True, null=True,
        on_delete=models.SET_NULL,
        )
    borrower = models.ForeignKey(
        User, related_name='Loan', blank=True, null=True,
        on_delete=models.CASCADE,
        )
    is_borrowed = models.BooleanField(
        default=False
        )


    def __str__(self):
        return self.name
