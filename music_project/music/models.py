from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

User._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'

# class Album(models.Model):
#     title = models.CharField(max_length=100)
#     artist = models.CharField(max_length=100)
#     release_date = models.DateField()

#     def __str__(self):
#         return self.title

# class Track(models.Model):
#     title = models.CharField(max_length=100)
#     album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
#     length = models.DurationField()

#     def __str__(self):
#         return self.title

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, blank=True)
    album = models.CharField(max_length=255, blank=True)
    song_file = models.CharField(max_length=250, blank=True)

class WatchLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
