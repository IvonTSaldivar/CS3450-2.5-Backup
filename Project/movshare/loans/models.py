from django.db import models
from movshare.users.models import User
from movshare.library.models import Media

# Create your models here.

class MediaRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE) # need to migrate stuff
    media = models.OneToOneField(Media, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
