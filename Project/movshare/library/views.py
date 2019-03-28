from django.shortcuts import render, redirect
from movshare.library.models import Shelf
from movshare.library.models import Media
from movshare.users.models import User
from .tables import SearchTable
from django_tables2 import RequestConfig
from django.contrib.auth import get_user_model
from django.db.models import Q
import urllib.parse

# Create your views here.

def ShelfView(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/?next=/library/shelf')
    if Shelf.objects.filter(owner=request.user).count() == 0 or Shelf.objects.filter(name='Default',
                                                                                     owner=request.user).count() == 0:
        shelf = Shelf(name='Default', owner=request.user)
        shelf.save()
    shelves = Shelf.objects.all()
    media = Media.objects.all()
    context = {'shelves': shelves,'media': media,}
    return render(request, 'pages/shelf.html', context,)

def HomeView(request):
    shelves = set([])

    if 'sort' in request.GET:
        sort = request.GET['sort']
    else:
        sort = 'name'

    media = Media.objects.order_by(sort)

    for medium in media:
        shelves.add(medium.shelf)

    if sort == 'owner':
        shelves=sorted(shelves,key=lambda x: x.owner.username, reverse=False)

    # if sort == 'type':
    #     for m in media:
    #         t = m
    #         t.owner = m.media_type


    context = {'shelves': shelves,'media': media,}
    return render(request, 'pages/home.html', context,)

# user_list_view = UserListView.as_view()

def AddMediaView(request):
    shelves = Shelf.objects.all();
    return render(request, 'pages/shelfViews/addmedia.html',
                  {
                      'shelves': shelves
                  }
                  )


def AddShelfView(request):
    return render(request, 'pages/shelfViews/addshelf.html')


def PostMedia(request):
    if request.method == 'POST':
        count = Media.objects.filter(name=request.POST.get('name'), owner=request.user).count()
        mediaName = ''
        if count != 0:
            mediaName = "%s (%d)" % (request.POST.get('name'), count)
        else:
            mediaName = request.POST.get('name')
        m = Media(name=mediaName,
                  owner=request.user,
                  media_type=request.POST.get('type'),
                  description=request.POST.get('description'),
                  shelf=Shelf.objects.get(name=request.POST.get('shelf'), owner=request.user))
        m.save()
    return redirect('library:shelf')


def PostShelf(request):
    if request.method == 'POST':
        count = Shelf.objects.filter(name=request.POST.get('name'), owner=request.user).count()
        shelfName = ''
        if count != 0:
            shelfName = "%s (%d)" % (request.POST.get('name'), count)
        else:
            shelfName = request.POST.get('name')
        s = Shelf(name=shelfName,
                  owner=request.user)
        s.save()
    return redirect('library:shelf')


def EncodedShelf(request, username, encoded_shelf):
    decoded = urllib.parse.unquote(encoded_shelf)
    shelf = Shelf.objects.get(name=decoded, owner=request.user)
    media = Media.objects.all()
    context = {'shelf': shelf, 'media': media, }
    return render(request, 'pages/shelfViews/expandedshelf.html', context,)

def ViewOnlyShelf(request, username, encoded_shelf):
    decodedShelf = urllib.parse.unquote(encoded_shelf)
    decodedUser = urllib.parse.unquote(username)
    print(decodedUser)
    user = User.objects.get(username=decodedUser)
    shelf = Shelf.objects.get(name=decodedShelf, owner=user)

    media = Media.objects.all()
    context = {'shelf': shelf, 'media': media, }
    return render(request, 'pages/shelfViews/viewonly.html',context,)


def DeleteMedia(request):
    media = Media.objects.get(name=request.POST.get('media_name'),
                              owner=request.user)
    encodedShelfName = request.POST.get('shelf_name')
    encodedUserName = request.POST.get('user_name')
    media.delete()
    destination = '/library/shelf/%s/%s' % (encodedUserName, encodedShelfName)
    return redirect(destination)


def DeleteShelf(request):
    current_shelf = Shelf.objects.get(name=request.POST.get('shelf_name'), owner=request.user)
    if current_shelf.name != 'Default':
        media = Media.objects.filter(shelf=current_shelf)
        default_shelf = Shelf.objects.get(name='Default', owner=request.user)
        for medium in media:
            medium.shelf = default_shelf
            medium.save()
        current_shelf.delete()
    return redirect('library:shelf')


def Search(request):
    search_term = ''
    if 'search' in request.GET and request.GET['search'] is not '':
        search_term = request.GET['search']
        media = Media.objects.filter(Q(name__icontains=search_term) | Q(media_type__icontains=search_term) | Q(
            description__icontains=search_term))
    else:
        media = Media.objects.none()

    table = SearchTable(media)
    RequestConfig(request).configure(table)

    return render(request, 'pages/search.html',
                  {
                      'search_term': search_term,
                      'table': table,
                  }
                  )
