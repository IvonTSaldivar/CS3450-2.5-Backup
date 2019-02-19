from django.shortcuts import render
from movshare.library.models import Shelf
from movshare.library.models import Media

# Create your views here.

def ShelfView(request):
    shelves = Shelf.objects.all();
    media = Media.objects.all();
    return render(request, 'pages/dashboard.html', 
                    {
                       'shelves': shelves,
                       'media': media
                     }
                 )

#user_list_view = UserListView.as_view()
