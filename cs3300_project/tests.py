from django.test import TestCase
from .models import Player, Clip

# Create your tests here.
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