from django.urls import path
from . import views

app_name = 'history'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),

##########
# ARTIST PATHS
    path('artists/', views.ArtistListView.as_view(), name='artists'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('artists/add/', views.ArtistFormView.as_view(), name='artist_form'),

##########
# ALBUM PATHS
    path('albums/', views.AlbumListView.as_view(), name='albums'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('albums/add/', views.AlbumFormView.as_view(), name='album_form'),

##########
# SONG PATHS
    path('songs/', views.SongListView.as_view(), name='song_list'),
    path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song_detail'),
    path('songs/add/', views.SongFormView.as_view(), name='song_form'),
]