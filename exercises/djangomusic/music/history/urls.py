from django.urls import path

from . import views

# app_name = 'history'
urlpatterns = [
    # ex: /history/
    path('', views.index, name = 'index'),
    # path('<int:artist_id>/', views.artist, name = 'artist'),
    path('<int:artist_id>/', views.songs, name='songs')
]
