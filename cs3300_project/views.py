from django.shortcuts import redirect, render
from django.views import generic

from .models import Clip, User

class ClipListView(generic.ListView):
    model = Clip
class ClipDetailView(generic.DetailView):
    model = Clip

# Create your views here.
#    def index(request): 
#        return render(request, 'cs3300_project/index.html') 

def account(request, user_id):
    user=User.objects.get(id=user_id)
    context = {'user':user }
    return render(request, 'cs3300_project/account.html', context)

def yourAccount(request):
    return account(request, 1)

def yourClips(request):
    return render(request, 'cs3300_project/clips.html')

def yourSaved(request):
    return render(request, 'cs3300_project/saved.html')