from django.test import TestCase
from .models import User, Clip

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="userTest1", summary="This is the test summary for user 1")
        User.objects.create(username="userTest2", summary="This is the test summary for user 2")
    
    def test_user_details(self):
        userTest1 = User.objects.get(username="userTest1")
        self.assertEqual(userTest1.username, "userTest1")
        self.assertEqual(userTest1.summary, "This is the test summary for user 1")
        userTest2 = User.objects.get(username="userTest2")
        self.assertEqual(userTest2.username, "userTest2")
        self.assertEqual(userTest2.summary, "This is the test summary for user 2")

class ClipTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="userTest1", summary="This is the test summary for user 1")
        Clip.objects.create(title="Val Ace", game="Valorant", description="This is a description", user=user)
    
    def test_clip_details(self):
        clipTest1 = Clip.objects.get(title="Val Ace")
        self.assertEqual(clipTest1.title, "Val Ace")
        self.assertEqual(clipTest1.game, "Valorant")
        self.assertEqual(clipTest1.description, "This is a description")
        self.assertEqual(clipTest1.user.username, "userTest1")