from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from cs3300_project.forms import ClipForm
from .models import Clip, User
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
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was successfully created for " + user)
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
def account(request, user_id):
    user=User.objects.get(id=user_id)
    context = {'user':user }
    return render(request, 'cs3300_project/account.html', context)

def yourAccount(request):
    return account(request, 1)

@login_required(login_url='login') # Only allowing people who are logged in to access this page
def yourClips(request):
    return render(request, 'cs3300_project/yourclips.html')

@login_required(login_url='login') # Only allowing people who are logged in to access this page
def yourSaved(request):
    return render(request, 'cs3300_project/saved.html')

def createClip(request, user_id):
    form = ClipForm()
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        # Create a new dictionary with form data and clip_id
        clip_data = request.POST.copy()
        clip_data['user_id'] = user_id

        form = ClipForm(clip_data)
        if form.is_valid():
            # Save the form without committing to the database
            clip = form.save(commit=False)
            # Set the user relationship
            clip.user = user
            clip.save()

            # Redirect back to the your clips page
            return redirect('yourClips')
        
    context = {'form': form}
    return render(request, 'cs3300_project/clip_form.html', context)

def updateClip(request, user_id, clip_id):
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

def deleteClip(request, user_id, clip_id):
    form = ClipForm()
    clip = Clip.objects.get(pk=clip_id)

    if request.method == 'POST':
        clip.delete()
        return redirect('yourClips')
    
    context = {'form': form, 'clip': clip}
    return render(request, 'cs3300_project/clip_delete_form.html', context)
