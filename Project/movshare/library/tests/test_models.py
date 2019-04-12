from django.test import TestCase
from django.test import Client

from ..models import Shelf
from ..models import Media
from ...users.models import User

# Create your tests here.

class LibraryModelsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='root', email='root@root.root', password='iamroot96!')
        self.borrower = User.objects.create(username='borrow', email='borrow@borrow.borrow', password='iamborrow96!')
        self.shelf = Shelf.objects.create(name="myShelf", owner=self.user)
        self.media = Media.objects.create(name="myMedia", media_type="movie", description="a movie", owner=self.user, borrower=self.borrower, isBorrowed=true, shelf=self.shelf)

    def test_shelf_model(self):
        self.assertEqual(self.shelf.name, "myShelf")
        self.assertEqual(self.shelf.owner, self.user)

    def test_media_model(self):
        self.assertEqual(self.media.name, "myMedia")
        self.assertEqual(self.media.media_type, "movie")
        self.assertEqual(self.media.description, "a movie")
        self.assertEqual(self.media.owner, self.user)
        self.assertEqual(self.media.borrower, self.borrower)
        self.assertEqual(self.media.isBorrowed, self.true)
        self.assertEqual(self.media.shelf, self.shelf)
