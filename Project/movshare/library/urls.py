from django.urls import path

from movshare.library.views import (
    ShelfView, AddMediaView, AddShelfView, 
	PostMedia, PostShelf, ExpandedShelf,
	EncodedShelf, DeleteMedia,
)

app_name = 'library'
urlpatterns = [
    path('shelf', view=ShelfView, name='shelf'),
	path('shelf/expand/<str:shelf_name>', view=ExpandedShelf, name='expandshelf'),
	path('shelf/<str:encoded_shelf>', view=EncodedShelf, name='encodedshelf'),
	path('addMedia', view=AddMediaView, name='addMedia'),
	path('addShelf', view=AddShelfView, name='addShelf'),
	path('newMedia', view=PostMedia, name='newMedia'),
	path('newShelf', view=PostShelf, name='newShelf'),
	path('deleteMedia', view=DeleteMedia, name='deleteMedia'),
]
