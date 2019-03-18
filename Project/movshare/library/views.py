from django.shortcuts import render, redirect
from movshare.library.models import Shelf
from movshare.library.models import Media
from django.contrib.auth import get_user_model
import urllib.parse


# Create your views here.

def ShelfView(request):
	search_term = ''
	shelves = Shelf.objects.all();
	media = Media.objects.all();
	if 'search' in request.GET:
		search_term = request.GET['search']
		media = Media.objects.filter(name__icontains = search_term)
		#shelves = media.shelf
	if shelves.filter(owner=request.user).count() == 0 or shelves.filter(name='Default', owner=request.user).count() == 0:
		shelf = Shelf(name='Default', owner=request.user)
		shelf.save()

	return render(request, 'pages/shelf.html', 
                    {
                       'shelves': Shelf.objects.all(),
                       'media': media,
                       'search_term': search_term
                    }
                )

#user_list_view = UserListView.as_view()

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
						shelf=Shelf.objects.get(name=request.POST.get('shelf')))
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
	shelf = Shelf.objects.get(name=decoded)
	medias = Media.objects.all()
	return render(request, 'pages/shelfViews/expandedshelf.html',
					{
						'shelf': shelf,
						'media': medias
					}
				)

def DeleteMedia(request):
	media = Media.objects.get(name=request.POST.get('media_name'),
					owner=request.user)
	shelfName = request.POST.get('shelf_name')
	media.delete()
	destination = '/library/shelf/%s' % (shelfName)
	return redirect(destination)
	
	
def DeleteShelf(request):
	print(request.POST.get('shelf_name'))
	current_shelf = Shelf.objects.get(name=request.POST.get('shelf_name'),
					owner=request.user)
	if current_shelf.name != 'Default':
		media = Media.objects.filter(shelf=current_shelf)
		default_shelf = Shelf.objects.get(name='Default', owner=request.user)
		for medium in media:
			medium.shelf = default_shelf
			medium.save()
		current_shelf.delete()
	return redirect('library:shelf')