import django_tables2 as tables
from .models import Media

class MediaTable(tables.Table):
    class Meta:
        model = Media
        template_name = 'django_tables2/bootstrap.html'
