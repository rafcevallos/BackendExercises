from django import forms
from .models import Artist, Album, Genre, Songs


# FORMS are used for USER input to add information to the Database
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artist_name']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'label', 'album_date']