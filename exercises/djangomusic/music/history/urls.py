from django.urls import path
from . import views

app_name = 'history'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('artists/', views.ArtistListView.as_view(), name='artists'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('artists/add/', views.ArtistFormView.as_view(), name='artist_form'),
    # path('<int:artist_id>/', views.artist, name = 'artist'),
    # path('<int:artist_id>/', views.songs, name='songs')
]
