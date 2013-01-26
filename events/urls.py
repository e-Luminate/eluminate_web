from django.conf.urls import patterns, url
from events import views

urlpatterns = patterns('',
    url(r'^$', views.root_dispatch, name = 'root'),
    url(r'^new/$', views.new, name = 'new'),
    url(r'^(?P<event_id>\d+)/$', views.show, name = 'show'),
    url(r'^(?P<event_id>\d+)/edit$', views.edit, name = 'show'),
)

