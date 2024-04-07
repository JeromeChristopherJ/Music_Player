from django.shortcuts import render, redirect
from datetime import date
from music.models import Song,WatchLater
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from music.forms import LoginForm, RegistrationForm

# def custom_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('album_list')  # Redirect to the album_list page after login
#             else:
#                 # Invalid credentials, display alert message
#                 return render(request, 'registration/login.html', {'form': form, 'invalid': True})
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})
def add_to_watch_later(request, song_id):
    if request.method == 'POST':
        user = request.user  
        song = Song.objects.get(pk=song_id)
        if(WatchLater.objects.filter(user=user, song=song).exists()):
            return redirect('watchlater')
        watch = WatchLater.objects.create(user=user, song=song)
        print(watch)
    return redirect('watchlater')  

def watch_later_list(request):
    user = request.user
    watch_later_songs = WatchLater.objects.filter(user=user)  # Optimize query with select_related
    context = {'watch_later_songs': watch_later_songs}
    return render(request, 'music/watchlater.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print("Done")
            if user:
                login(request)
                return redirect('album_list') 
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'music/login.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to the login page after successful registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = RegistrationForm()
    return render(request, 'music/register.html', {'form': form})

# def logout_view(request):
#     logout(request)
#     return redirect('home')

def album_list(request):
  songs = Song.objects.all()
  search_query = request.GET.get('query', '')
  if(request.user.is_anonymous == False):
    user = request.user
    watch_later_songs = WatchLater.objects.filter(user=user)
  else:
    watch_later_songs = []

  watch_later_list = []

  for watch_later in watch_later_songs:
      watch_later_list.append(watch_later.song)
  if search_query:
    songs = songs.filter(title__icontains=search_query)
  context = {'songs': songs, 'search_query': search_query, 'current_year': date.today().year, 'watch_later': watch_later_list}
  return render(request, 'music/album_list.html', context)


# def album_list(request):
#     albums = Album.objects.all()
#     return render(request, 'music/album_list.html', {'albums': albums})
def logout(request):
    logout(request)
    return redirect('album_list')

def about(request):
  return render(request, 'music/about.html')