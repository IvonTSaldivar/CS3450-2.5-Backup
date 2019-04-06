from django.urls import path

from movshare.loans.views import(requestsView, requestMedia)

app_name = 'loans'
urlpatterns = [
    path('addRequest', view=requestMedia, name='requestMedia' ),
    path('requests', view=requestsView, name='requests')
]
