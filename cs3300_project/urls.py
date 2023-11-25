from .views import ClipListView, ClipDetailView
from django.urls import include, path 
from . import views 

urlpatterns = [ 
    # path function defines a url pattern 
    # '' is empty to represent based path to app 
    # views.index is the function defined in views.py 
    # name = 'index' parameter is to dynamically create url
    path("__reload__/", include("django_browser_reload.urls")),   
    #path('', views.index, name='index'),
    path ('', ClipListView.as_view(), name='index'),
    path('clips/<int:pk>', ClipDetailView.as_view(), name='clip-detail'),
    path('player/<int:player_id>/', views.account, name='account'), # Accessing someone else's account
    path('player/', views.yourAccount, name='yourAccount'), # Accessing your own account
    path('player/<int:player_id>/update_player/', views.updatePlayer, name='update_player'), # Updating your account
    path('player/yourclips', views.yourClips, name='yourClips'), # Accessing your own clips
    path('player/<int:player_id>/create_clip/', views.createClip, name='create_clip'), # Creating a clip
    path('player/<int:player_id>/update_clip/<int:clip_id>', views.updateClip, name='update_clip'), # Updating a clip
    path('player/<int:player_id>/delete_clip/<int:clip_id>', views.deleteClip, name='delete_clip'), # Deleting a clip
    path('player/saved', views.yourSaved, name='yourSaved'), # Accessing your saved clips
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
] 