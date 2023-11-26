from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from cs3300_project.forms import ClipForm, PlayerForm
from .models import Clip, Player
from .forms import CreateUserForm

class ClipListView(generic.ListView):
    model = Clip
class ClipDetailView(generic.DetailView):
    model = Clip

# Create your views here.
#    def index(request): 
#        return render(request, 'cs3300_project/index.html') 

# Views for user authentification
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            player = Player.objects.create(username=username, user=user)
            player.save()
            messages.success(request, "Account was successfully created for " + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('yourClips')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('login')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# Other views
def account(request, player_id):
    player=Player.objects.get(id=player_id)
    context = {'player':player }
    return render(request, 'cs3300_project/account.html', context)

# Accessing the information for your own account
@login_required(login_url='login') # Only allowing people who are logged in to access this page
def yourAccount(request):
    player = request.user.player 
    return account(request, player.id) 

@login_required(login_url='login') # Only allowing people who are logged in to access this page
def yourClips(request):
    # Assuming there is one clip instance to get the choices (yikes)
    clip_instance = Clip.objects.first()
    available_games = dict(clip_instance._meta.get_field('game').choices)

    # Add more context by adding the player
    player = request.user.player

    # Get the clips associated with the current player (querying)
    clip_list = Clip.objects.filter(player=player)

    context = {'available_games': available_games, 'player': player, 'clip_list': clip_list}
    return render(request, 'cs3300_project/yourclips.html', context)

@login_required(login_url='login') # Only allowing people who are logged in to access this page
def yourSaved(request):
    return render(request, 'cs3300_project/saved.html')

# Code for creating, updating, and deleting a clip
def createClip(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    form = ClipForm()
    player = Player.objects.get(pk=player_id)

    if request.method == 'POST':
        # Create a new dictionary with form data and clip_id
        clip_data = request.POST.copy()
        clip_data['player_id'] = player_id

        form = ClipForm(clip_data)
        if form.is_valid():
            # Save the form without committing to the database
            clip = form.save(commit=False)
            # Set the player relationship
            clip.player = player
            clip.save()

            # Redirect back to the your clips page
            return redirect('yourClips')
        
    context = {'form': form}
    return render(request, 'cs3300_project/clip_form.html', context)

def updateClip(request, player_id, clip_id):
    clip = Clip.objects.get(pk=clip_id)
    form = ClipForm(instance=clip)

    if request.method == 'POST':
        clip_data = request.POST.copy()
        form=ClipForm(clip_data, instance=clip) # Autofills the data

        if form.is_valid():
            clip.title=form.cleaned_data['title']
            clip.game=form.cleaned_data['game']
            clip.description=form.cleaned_data['description']
            clip.save()
            return redirect('yourClips')
        
    context = {'form': form, 'clip': clip}
    return render(request, 'cs3300_project/clip_form.html', context)

def deleteClip(request, player_id, clip_id):
    form = ClipForm()
    clip = Clip.objects.get(pk=clip_id)

    if request.method == 'POST':
        clip.delete()
        return redirect('yourClips')
    
    context = {'form': form, 'clip': clip}
    return render(request, 'cs3300_project/clip_delete_form.html', context)

def updatePlayer(request, player_id):
    player = Player.objects.get(pk=player_id)
    form = PlayerForm(instance=player)

    if request.method == 'POST':
        player_data = request.POST.copy()
        form=PlayerForm(player_data, instance=player) # Autofills the data

        if form.is_valid():
            player.username=form.cleaned_data['username']
            player.summary=form.cleaned_data['summary']
            player.user.username=form.cleaned_data['username']
        
            # Update player's User username
            player.save()
            player.user.save()
            return redirect('yourAccount')
        
    context = {'form': form, 'player': player}
    return render(request, 'cs3300_project/player_form.html', context)

