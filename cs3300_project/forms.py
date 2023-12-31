from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Clip, Player

# Create forms here
class ClipForm(ModelForm):
    class Meta:
        model = Clip
        fields = ('title', 'game', 'description') 

# Could define a custom form here for a Player, (make sure to look back at the slides for how to do that...with user thing)
class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ('username', 'summary')
        exclude=['user']

# User creation form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

