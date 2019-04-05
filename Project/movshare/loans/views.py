from django.shortcuts import render, redirect
from movshare.library.models import Media
from movshare.loans.models import MediaRequest
from movshare.users.models import User
from .tables import RequestTable
from django_tables2 import RequestConfig
from django.contrib.auth import get_user_model
from django.db.models import Q
import urllib.parse

# Create your views here.

# view for requests screen
def requestsView(request, username):
    media = set([])
    theRequests = MediaRequest.objects.filter(requester= request.user)

    for medium in Media.objects.all():
        if medium.shelf == shelf:
            media.add(medium)

    table = ExpandedShelfTable(media)
    RequestConfig(request).configure(table)

    context = {'shelf': shelf, 'media': media, 'table': table,}
    return render(request, 'pages/requests/requests.html', context,)

# api for adding request to database
def requestMedia(request):
    print(str(request.method))
    if request.method == 'POST':
        requester = request.user
        print(str(requester))
        print(request.POST.get('media_name'))
        print(request.POST.get('media_owner'))
        #media = Media.abjects.get(name= request.POST.get('media_name'), owner= request.POST('media_owner')
    return redirect('library:shelf')
# api for approving request.
