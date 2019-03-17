from django.shortcuts import render, redirect
from movshare.library.models import Shelf
from movshare.library.models import Media
from django.contrib.auth import get_user_model
import urllib.parse


# Create your views here.

def ShelfView(request):
    shelves = Shelf.objects.all();
    media = Media.objects.all();
    return render(request, 'pages/shelf.html', 
                    {
                       'shelves': shelves,
                       'media': media
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
	
def ExpandedShelf(request, shelf_name):
	encoded = urllib.parse.quote_plus(shelf_name)
	print('encoding!')
	return redirect('library:encodedshelf',	encoded_shelf=encoded)
	
def EncodedShelf(request, encoded_shelf):
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
		