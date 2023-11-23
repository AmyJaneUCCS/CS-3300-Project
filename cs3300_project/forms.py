from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from .models import Clip

# Create forms here
class ClipForm(ModelForm):
    class Meta:
        model = Clip
        fields = ('title', 'game', 'description') 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

