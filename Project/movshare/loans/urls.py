from django.urls import path

from movshare.loans.views import(requestsView, requestMedia, approveMedia)

app_name = 'loans'
urlpatterns = [
    path('approveMedia', view=approveMedia, name='approveMedia'),
    path('addRequest', view=requestMedia, name='requestMedia' ),
    path('requests', view=requestsView, name='requests')
]
