from django_tables2 import tables, TemplateColumn
from .models import Media

class SearchTable(tables.Table):
    class Meta:
        model = Media
        attrs = {'class': 'table table-sm'}
        fields = ['name', 'media_type', 'description', 'owner', 'shelf', 'loan']
        template_name = 'django_tables2/bootstrap.html'
    loan = TemplateColumn(template_name='pages/tables/loanrequestbtn.html')

class ExpandedShelfTable(tables.Table):
    class Meta:
        model = Media
        attrs = {'class': 'table table-sm'}
        fields = ['name', 'media_type', 'description', 'delete']
        template_name = 'django_tables2/bootstrap.html'
    delete = TemplateColumn(template_name='pages/tables/deletemediabtn.html')
