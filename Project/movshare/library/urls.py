from django.urls import path

from movshare.library.views import (
    ShelfView,
)

app_name = "library"
urlpatterns = [
    path("shelf", view=ShelfView, name="shelf"),
]
