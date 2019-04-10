from django.urls import path

from movshare.loans.views import(requestsView, requestMedia, approveMedia)

app_name = 'loans'
urlpatterns = [
    path('addRequest', view=requestMedia, name='requestMedia' ),
    path('requests', view=requestsView, name='requests'),
    path('approveMedia', view=approveMedia, name='approveMedia')
]
