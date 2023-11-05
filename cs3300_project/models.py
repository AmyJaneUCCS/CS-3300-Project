from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    summary = models.TextField(blank=False)


    # Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clip-detail', args=[str(self.id)])
    

class Clip(models.Model):

    #List of choices for major value in database, human readable name
    GAME = (
        ('APEX', 'Apex'),
        ('RL', 'Rocket League'),
        ('VALORANT', 'Valorant'),
    )
    title = models.CharField(max_length=200)
    game = models.CharField(max_length=200, choices=GAME)
    description = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)    # A clip has a singular user

    # Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    # Returns the URL to access a particular instance of MyModelName.
    # if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('clip-detail', args=[str(self.id)])
    