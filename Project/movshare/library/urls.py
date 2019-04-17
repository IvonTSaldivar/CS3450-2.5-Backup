from django.urls import path

from movshare.library.views import (
    ShelfView, AddMediaView, AddShelfView,
    PostMedia, PostShelf, Search,
    EncodedShelf, ViewOnlyShelf, DeleteMedia, DeleteShelf, IMDBSearch,
    viewAll
)

app_name = 'library'
urlpatterns = [
    path('shelf', view=ShelfView, name='shelf'),
    path('shelf/<str:username>/<str:encoded_shelf>', view=EncodedShelf, name='encodedshelf'),
    path('shelf/view/<str:username>/<str:encoded_shelf>', view=ViewOnlyShelf, name='viewonlyshelf'),
    path('addMedia', view=AddMediaView, name='addMedia'),
    path('addShelf', view=AddShelfView, name='addShelf'),
    path('newMedia', view=PostMedia, name='newMedia'),
    path('newShelf', view=PostShelf, name='newShelf'),
    path('deleteMedia', view=DeleteMedia, name='deleteMedia'),
    path('deleteShelf', view=DeleteShelf, name='deleteShelf'),
    path('search', view=Search, name='search'),
    path('IMDBsearch', view=IMDBSearch, name='IMDBsearch'),
    path('viewAll', view=viewAll, name='viewAll'),
    path('', view=ShelfView, name='home'),
]

