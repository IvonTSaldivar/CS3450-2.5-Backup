from django.test import TestCase
from django.test import Client
from django.conf import settings

from ..models import Shelf
from ..models import Media
from ...users.models import User

# Create your tests here.

class LibraryViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='root', email='root@root.root', password='iamroot96!')
        self.credentials = {'username': 'root', 'password': 'iamroot96'}

    def test_shelf_view(self):
        redirect_response = self.client.get('/library/shelf')
        self.assertEqual(redirect_response.status_code, 302)
        login_response = self.client.post('/accounts/login/', **self.credentials)
        view_response = self.client.get('/library/shelf')
        self.assertEqual(view_response.status_code, 200)

    def test_add_media_view(self):
        view_response = self.client.get('/library/addMedia')
        self.assertEqual(view_response.status_code, 200)

    def test_add_shelf_view(self):
        view_response = self.client.get('/library/addShelf')
        self.assertEqual(view_response.status_code, 200)

    def test_home_view(self):
        login_response = self.client.post('/accounts/login/', **self.credentials)
        view_response = self.client.get('/library')
        self.assertEqual(view_response.status_code, 200)

    def test_delete_shelf_view(self):
        self.shelf = Shelf.objects.create(name="myShelf", owner=self.user)
        self.media = Media.objects.create(name="myMedia", media_type="movie", description="a movie", owner=self.user, shelf=self.shelf)
        params = {'shelf_name': 'myShelf'}
        view_response = self.client.post('/library/deleteShelf', **params)
        self.assertEqual(view_response.status_code, 200)

    def test_delete_media_view(self):
        self.shelf = Shelf.objects.create(name="myShelf", owner=self.user)
        self.media = Media.objects.create(name="myMedia", media_type="movie", description="a movie", owner=self.user, shelf=self.shelf)
        params = {'media_name': 'myMedia'}
        view_response = self.client.post('/library/deleteMedia', **params)
        self.assertEqual(view_response.status_code, 200)

    def test_search_view(self):
        view_response = self.client.get('/library/search')
        self.assertEqual(view_response.status_code, 200)
