from django.urls import path

from movshare.loans.views import(requestsView, requestMedia, approveMedia, borrowed, return_media)

app_name = 'loans'
urlpatterns = [
    path('approveMedia', view=approveMedia, name='approveMedia'),
    path('addRequest', view=requestMedia, name='requestMedia' ),
    path('requests', view=requestsView, name='requests'),
    path('borrowed', view=borrowed, name='borrowed'),
    path('return_media', view=return_media, name='return_media')
]
