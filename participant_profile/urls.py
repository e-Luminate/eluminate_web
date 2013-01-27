from django.conf.urls import patterns, url
from participant_profile import views

urlpatterns = patterns('',
    url(r'^$', views.root_dispatch, name = 'root'),
    url(r'^events/$', views.events_dispatch, name = 'events'),
    url(r'^events/new/$', views.events_new, name = 'events_new'),
    url(r'^events/(?P<event_id>\d+)/$', views.events_item_dispatch, name = 'events_item'),
    url(r'^events/(?P<event_id>\d+)/edit/$', views.events_edit, name = 'events_edit'),
)

