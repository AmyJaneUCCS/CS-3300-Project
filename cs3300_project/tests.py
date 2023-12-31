from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Player, Clip


# Test if any user can go to the different pages
class CheckPages(TestCase):
    def setUp(self):
        User.objects.create_user(username="testUser", email="testemail@gmail.com", password="somepass89")

    def test_login_page(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
    
    # Testing if the user is not logged out
    def test_logout_page(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
    
    def test_yourclips_page(self):
        response = self.client.get('/player/yourclips')
        self.assertEqual(response.status_code, 302)
    
    def test_saved(self):
        response = self.client.get('/player/saved')
        self.assertEqual(response.status_code, 302)
    
    def test_account_page(self):
        response = self.client.get('/player/')
        self.assertEqual(response.status_code, 302)

# Unit test for the User
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testUser", email="testemail@gmail.com", password ="somepass89")
    
    def test_user_details(self):
        userTest1 = User.objects.get(username="testUser")
        self.assertEqual(userTest1.username, "testUser")
        self.assertEqual(userTest1.email, "testemail@gmail.com")
        self.assertEqual(userTest1.password, "somepass89")
        
# Unit tests for the Player and Clip models
class PlayerTestCase(TestCase):
    def setUp(self):
        Player.objects.create(username="playerTest1", summary="This is the test summary for player 1")
        Player.objects.create(username="playerTest2", summary="This is the test summary for player 2")
    
    def test_player_details(self):
        playerTest1 = Player.objects.get(username="playerTest1")
        self.assertEqual(playerTest1.username, "playerTest1")
        self.assertEqual(playerTest1.summary, "This is the test summary for player 1")
        playerTest2 = Player.objects.get(username="playerTest2")
        self.assertEqual(playerTest2.username, "playerTest2")
        self.assertEqual(playerTest2.summary, "This is the test summary for player 2")

class ClipTestCase(TestCase):
    def setUp(self):
        player = Player.objects.create(username="playerTest1", summary="This is the test summary for player 1")
        Clip.objects.create(title="Val Ace", game="Valorant", description="This is a description", player=player)
    
    def test_clip_details(self):
        clipTest1 = Clip.objects.get(title="Val Ace")
        self.assertEqual(clipTest1.title, "Val Ace")
        self.assertEqual(clipTest1.game, "Valorant")
        self.assertEqual(clipTest1.description, "This is a description")
        self.assertEqual(clipTest1.player.username, "playerTest1")