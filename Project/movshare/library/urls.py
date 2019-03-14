from django.urls import path

from movshare.library.views import (
    ShelfView, AddMediaView, AddShelfView, PostMedia, PostShelf,
)

app_name = "library"
urlpatterns = [
    path("shelf", view=ShelfView, name="shelf"),
	path("addMedia", view=AddMediaView, name="addMedia"),
	path("addShelf", view=AddShelfView, name="addShelf"),
	path("newMedia", view=PostMedia, name="newMedia"),
	path("newShelf", view=PostShelf, name="newShelf"),

]
