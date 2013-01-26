from django.conf import settings
from django.conf.urls import  patterns, url

urlpatterns = patterns('maps.views',
                       url(r'^$', 'list', name='locations_list'),
                       url(r'edit/(\d+)', 'edit', name='edit_location'),
                       url(r'add', 'add', name='add_location'),
                       url(r'delete/(\d+)', 'delete', name='delete_location'),
)