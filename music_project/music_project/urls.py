"""
URL configuration for music_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from music import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('music/', include('music.urls')),
#     path('', views.album_list, name='home'),
#     path('search/', views.album_list, name='search'),
#     # path('accounts/login/', custom_login, name='login'), 
#     path('login/', views.login_view, name='login'),
#     path('register/', views.register_view, name='register'), 
#     path('accounts/', include('django.contrib.auth.urls')),  
#     # path('register/', register, name='register'),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('music.urls')),
    path('', views.album_list, name='album_list'),
    path('search/', views.album_list, name='search'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    #path('about/', views.about, name='about'),
    path('watchlater/', views.watch_later_list, name='watchlater'),
    path('addtowatchlater/<int:song_id>/', views.add_to_watch_later, name='addtowatchlater')
]