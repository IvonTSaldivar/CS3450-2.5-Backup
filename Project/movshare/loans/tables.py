from django_tables2 import tables, TemplateColumn
from .models import MediaRequest, Media

class RequestTable(tables.Table):
    class Meta:
        model = MediaRequest
        attrs = {'class': 'table table-sm'}
        fields = ['requester', 'media.name', 'media.media_type', 'media.description']
        template_name = 'django_tables2/bootstrap.html'
    approve = TemplateColumn(template_name = 'pages/tables/approvebtn.html')

class BorrowedTable(tables.Table):
    class Meta:
        model = Media
        attrs = {'class': 'table table-sm'}
        fields = ['owner', 'name', 'media_type', 'description']
        template_name = 'django_tables2/bootstrap.html'
    return_media = TemplateColumn(template_name = 'pages/tables/returnbtn.html')


