from django.shortcuts import render, redirect
from movshare.library.models import Shelf
from movshare.library.models import Media
from movshare.users.models import User
from .tables import SearchTable, ExpandedShelfTable, IMDBSearchTable, ViewAllTable
from django_tables2 import RequestConfig
from django.contrib.auth import get_user_model
from django.db.models import Q
import urllib.parse

from imdbpie import ImdbFacade
from imdbpie import Imdb

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
        sort = 'name' #this is the default sort

    media = Media.objects.order_by(sort)

    for medium in media:
        if(medium.owner != request.user):
            shelves.add(medium.shelf)

    if sort == 'owner':
        shelves=sorted(shelves,key=lambda x: x.owner.username, reverse=False)

    context = {'shelves': shelves,'media': media,}
    return render(request, 'pages/home.html', context,)

# user_list_view = UserListView.as_view()

def viewAll(request):
    media = set([])
    owners = User(name ="All")
    shelf = Shelf(name='All', owner=owners)

    for medium in Media.objects.all():
        media.add(medium)

    table = ViewAllTable(media)


    RequestConfig(request).configure(table)
    print("here!")
    context = {'shelf': shelf, 'media': media, 'table': table,}
    return render(request, 'pages/shelfViews/viewonly.html',context,)


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
        print(count)
        if count != 0:
            newCount = 1
            while newCount != 0:
                newCount = Media.objects.filter(name=request.POST.get('name') + ' (' + str(count) + ')', owner=request.user).count()
                count += newCount 
            mediaName = "%s (%d)" % (request.POST.get('name'), count)
        else:
            mediaName = request.POST.get('name')
        if mediaName != '':

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
        if shelfName != '':
            s = Shelf(name=shelfName,
                     owner=request.user)
            s.save()
    return redirect('library:shelf')


def EncodedShelf(request, username, encoded_shelf):
    media = set([])
    decoded = urllib.parse.unquote(encoded_shelf)
    shelf = Shelf.objects.get(name=decoded, owner=request.user)

    for medium in Media.objects.all():
        if medium.shelf == shelf:
            media.add(medium)

    table = ExpandedShelfTable(media)


    RequestConfig(request).configure(table)

    context = {'shelf': shelf, 'media': media, 'table': table,}
    return render(request, 'pages/shelfViews/expandedshelf.html', context,)

def ViewOnlyShelf(request, username, encoded_shelf):
    media = set([])
    decodedShelf = urllib.parse.unquote(encoded_shelf)
    decodedUser = urllib.parse.unquote(username)
    user = User.objects.get(username=decodedUser)
    shelf = Shelf.objects.get(name=decodedShelf, owner=user)

    for medium in Media.objects.all():
        if medium.shelf == shelf:
            media.add(medium)

    table = SearchTable(media)
    RequestConfig(request).configure(table)

    context = {'shelf': shelf, 'table': table,}
    return render(request, 'pages/shelfViews/viewonly.html',context,)


def DeleteMedia(request):
    media = Media.objects.filter(name=request.POST.get('media_name'),
                              owner=request.user).first()
    encodedShelfName = request.POST.get('shelf_name')
    encodedUserName = request.POST.get('user_name')
    if media is not None:
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

    search_count = media.count()
    table = SearchTable(media)
    RequestConfig(request).configure(table)

    search_count = media.count()
    table = SearchTable(media)
    RequestConfig(request).configure(table)

    return render(request, 'pages/search.html',
                  {
                      'search_term': search_term,
                      'table': table,
                      'search_count' : search_count
                  }
                  )

def IMDBSearch(request):
    client = Imdb(locale='en_US')
    imdb = ImdbFacade(client=client)
    imdb2 = Imdb()
    results2 = set([])

    search_term = ''

    if 'search' in request.GET and request.GET['search'] is not '':
        search_term = request.GET['search']

        results = imdb2.search_for_title(search_term)
    else:
        results = Media.objects.none()

    ## Attempting to get the more detailed information, It works, sorta, but it'a really slow.
    # for r in results:
    #     results2.add(r.imdb_id)
    # for r in results2:
    #     print(imdb2.get_title(r)

    table = IMDBSearchTable(results)
    RequestConfig(request).configure(table)

    return render(request, 'pages/IMDBsearch.html',
                  {
                      'search_term': search_term,
                      'table': table,
                  }
                  )
