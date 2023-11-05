from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, 'cs3300_project/index.html') 

def account(request, user_id):
    return render(request, 'cs3300_project/account.html')

def yourAccount(request):
    return account(request, 1)

def yourClips(request):
    return render(request, 'cs3300_project/clips.html')

def yourSaved(request):
    return render(request, 'cs3300_project/saved.html')