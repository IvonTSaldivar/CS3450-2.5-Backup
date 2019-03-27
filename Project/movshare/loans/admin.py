from django.contrib import admin

# Register your models here.

from django.contrib import admin

from movshare.loans.models import MediaRequest

@admin.register(MediaRequest)
class MediaRequestAdmin(admin.ModelAdmin):
    list_display = ('requester','media', 'message')

