from django.test import TestCase

from ..models import MediaRequest
from ...library.models import Media
from ...library.models import Shelf
from ...users.models import User

# Create your tests here.

class LoansModelsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='root', email='root@root.root', password='iamroot96!')
        self.shelf = Shelf.objects.create(name="myShelf", owner=self.user)
        self.media = Media.objects.create(name="myMedia", media_type="movie", description="a movie", owner=self.user, shelf=self.shelf)
        self.media_request = MediaRequest.objects.create(requester=self.user, media=self.media, message="yo bro can I borrow this?")

    def test_media_request_model(self):
        self.assertEqual(self.media_request.requester, self.user)
        self.assertEqual(self.media_request.media, self.media )
        self.assertEqual(self.media_request.message, "yo bro can I borrow this?")
