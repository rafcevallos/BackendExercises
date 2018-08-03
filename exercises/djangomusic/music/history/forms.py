from django.forms import forms
from .models import Artist, Album, Genre, Songs


# Create the Artist form class
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artist_name']

#  Creating a form to add an Artist
form = ArtistForm()

# Creaiing a form to change an existing Artist
artist = Artist.objects.get(pk=1)
form = ArtistForm(instance=artist)


# Create the Album form class
class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'album_date', 'label', 'artist']

#  Creating a form to add an Album
form = AlbumForm()

# Creaiing a form to change an existing Album
album = Album.objects.get(pk=1)
form = AlbumForm(instance=album)