# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# from django.template import loader
from django.views.generic import ListView, FormView, DetailView, CreateView, TemplateView
from .models import Artist, Songs, Album, Genre
from .forms import ArtistForm, AlbumForm, SongForm


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
    form_class = ArtistForm
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


# ===============================
# ALBUM Views
class AlbumListView(ListView):
    model = Album
    context_object_name = 'album_list' #this allows you to change object_list into a readable and easy to access variable from templates

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "albums"
        return context # A Context is a dictionary with variable names as the "key" and their values as the "value"

class AlbumFormView(FormView):
    template_name = 'history/album_form.html'
    form_class = AlbumForm
    success_url = '/history/albums/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "albums"
        return context

    def form_valid(self, form):
        form.save()
        return super(AlbumFormView, self).form_valid(form)

class AlbumDetailView(DetailView):
    model = Album


# ===============================
# SONG Views
class SongListView(ListView):
    model = Songs
    context_object_name = 'song_list' #this allows you to change object_list into a readable and easy to access variable from templates

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "songs"
        return context # A Context is a dictionary with variable names as the "key" and their values as the "value"


class SongFormView(FormView):
    template_name = 'history/song_form.html'
    form_class = SongForm
    success_url = '/history/songs/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "songs"
        return context

    def form_valid(self, form):
        form.save()
        return super(SongFormView, self).form_valid(form)


class SongDetailView(DetailView):
    model = Songs