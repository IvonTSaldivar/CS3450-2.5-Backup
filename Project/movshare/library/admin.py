from django.contrib import admin

from movshare.library.models import Shelf, Media


@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'media_type', 'owner', 'shelf',)
