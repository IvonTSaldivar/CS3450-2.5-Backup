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
    media_type = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User, related_name='Media', blank=True, null=True,
        on_delete=models.CASCADE,
        )
    shelf = models.ForeignKey(
        Shelf, related_name='Media', blank=True, null=True,
        on_delete=models.SET_NULL,
        )

    def __str__(self):
        return self.name
