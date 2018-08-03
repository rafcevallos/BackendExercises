from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic import ListView, FormView, DetailView, CreateView
from .models import Artist, Songs, Album, Genre


class IndexView(TemplateView):
    template_name = 'history/index.html'

    def location(self):
        return 'home'

# ===============================
# ARTIST Views
class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artist_list' #this allows you to change object_list into a readable and easy to access variable from templates

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "artists"
        return context # A Context is a dictionary with variable names as the "key" and their values as the "value"

class ArtistFormView(FormView):
    template_name = 'history/artist_form.html'
    form_class = ArtistFormView
    success_url = '/history/artists/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "artists"
        return context

    def form_valid(self, form):
        form.save()
        return super(ArtistFormView, self).form_valid(form)

class ArtistDetailView(DetailView):
    model = Artist


def songs(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    songs = artist.songs_set.all()
    return render(request,'history/songs.html', {'artist': artist, 'songs': songs})