# music/urls.py
from django.urls import path
from music import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
] 
