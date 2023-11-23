from django.forms import ModelForm 
from .models import Clip

# Create forms here
class ClipForm(ModelForm):
    class Meta:
        model = Clip
        fields = ('title', 'game', 'description') 