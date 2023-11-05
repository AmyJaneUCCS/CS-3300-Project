from django.urls import path 
from . import views 

urlpatterns = [ 
    # path function defines a url pattern 
    # '' is empty to represent based path to app 
    # views.index is the function defined in views.py 
    # name = 'index' parameter is to dynamically create url   
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.account, name='account'), # Accessing someone else's account
    path('user/', views.yourAccount, name='yourAccount'), # Accessing your own account
    path('user/clips', views.yourClips, name='yourClips'), # Accessing your own clips
    path('user/saved', views.yourSaved, name='yourSaved'), # Accessing your saved clips
] 