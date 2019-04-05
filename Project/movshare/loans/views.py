from django.shortcuts import render, redirect
from movshare.library.models import Media
from movshare.loans.models import MediaRequest
from movshare.users.models import User
from django.contrib.auth.models import AbstractUser
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
    if request.method == 'POST' and str(request.user) != 'AnonymousUser':
        requester = request.user.username
        mediaName = urllib.parse.unquote(request.POST.get('media_name'))

        mediaOwner = User.objects.get(username = request.POST.get('media_owner'))

        mediaOwnerAll = User.objects.all()
        for m in mediaOwnerAll:
            print("name:")
            print(m.username)


        print(urllib.parse.unquote(request.POST.get('media_name')))
        print(str(requester))
        print(request.POST.get('media_owner'))

        count = MediaRequest.objects.filter(media = Media.objects.get(name = mediaName, owner = mediaOwner)).count()

        if count == 0:
            r = MediaRequest(requester = request.user,
                                 media = Media.objects.get(name = mediaName, owner = mediaOwner),
                                 message = "")
            r.save()
            print("saved")
    return redirect('library:shelf')
# api for approving request.
