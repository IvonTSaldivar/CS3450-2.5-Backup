from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
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
def requestsView(request):
    #redirect if not logged in not working not sure why. May need to register loans as an app?
    if not request.user.is_authenticated:
        return redirect('/accounts/login/?next=loans/requests')
    media = set([])
    print(request.user)
    if(str(request.user) != 'AnonymousUser'):
        theRequests = MediaRequest.objects.filter(requester= request.user)

        for r in theRequests:
            media.add(r)
            print(r.media.owner)
            print(r.media.name)


        table = RequestTable(media)
        RequestConfig(request).configure(table)
        #context = {'shelf': shelf, 'media': media, 'table': table,}
        context = {'table': table}
        return render(request, 'pages/requests/requests.html', context)
    return redirect('home')
    #return render(request, 'pages/requests/requests.html', context,)

# api for adding request to database
def requestMedia(request):
    print(str(request.method))
    owner = request.POST.get('media_owner')
    shelf = request.POST.get('shelf_name')
    if request.method == 'POST' and str(request.user) != 'AnonymousUser':
        requester = request.user.username
        mediaOwner = User.objects.get(username = request.POST.get('media_owner'))
        if requester != request.POST.get('media_owner'):
            mediaName = urllib.parse.unquote(request.POST.get('media_name'))

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
    destination = '/library/shelf/view/%s/%s' %(owner, shelf)
    return redirect(destination)

# api for approving request.
def approveMedia(request):


    return redirect('library:shelf')

# api for rejecting request.

# api for approving request
