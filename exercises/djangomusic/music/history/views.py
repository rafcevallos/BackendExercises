from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Artist, Songs

# Create your views here.


def index(request):
    latest_question_list = Artist.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'history/index.html', context)


# def artist(request, artist_id):
#     artist = get_object_or_404(Artist, pk=artist_id)
#     return render(request, 'history/artist.html', {'artist': artist})

def songs(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    songs = artist.songs_set.all()
    return render(request,'history/songs.html', {'artist': artist, 'songs': songs})
