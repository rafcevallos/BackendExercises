# import datetime
from django.db import models
from django.utils import timezone


# Artist Model
class Artist(models.Model):
    artist_name = models.CharField(default="", max_length=200)
    # pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.artist_name

#  Album Model
class Album(models.Model):
    title = models.CharField(default="", max_length=200)
    album_date = models.DateField(auto_now=False, auto_now_add=False)
    label = models.CharField(default="", max_length=30)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.title)

# Genre Modle
class Genre(models.Model):
    style = models.CharField(default="", max_length=30)

    def __str__(self):
        return "{0}".format(self.style)

# Genre Songs
class Songs(models.Model):
    title = models.CharField(default="", max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.title)