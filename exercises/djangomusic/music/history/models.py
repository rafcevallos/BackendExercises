import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.artist_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Songs(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_text = models.CharField(max_length=200)
    lyrics = models.CharField(max_length=2000)

    def __str__(self):
        return self.song_text
