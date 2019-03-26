# from django.contrib import admin
#
## Register your models here.
#
# from django.contrib.auth import admin as auth_admin
# from movshare.users.forms import UserChangeForm, UserCreationForm
#
# User = get_user_model()
#
#
# @admin.register(User)
# class ShelfAdmin(auth_admin.ShelfAdmin):
#
#    add_form = UserCreationForm
#    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
#    list_display = ["username", "name", "is_superuser"]
#    search_fields = ["name"]

from django.contrib import admin

from movshare.library.models import Shelf, Media


@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'media_type', 'owner', 'shelf',)
