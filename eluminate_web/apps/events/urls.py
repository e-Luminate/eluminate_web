from django.conf.urls import patterns, url
from .views import EventDetail, EventList, EventCreate, EventUpdate, EventDelete

urlpatterns = patterns('',
    url(r'^$', EventList.as_view(), name ='events-list'),
    url(r'^create$', EventCreate.as_view(), name="event-create"),
    url(r'^(?P<pk>\d+)/$', EventDetail.as_view(), name ='event-detail'),
    url(r'^(?P<pk>\d+)/update', EventUpdate.as_view(), name = "event-update"),
    url(r'^(?P<pk>\d+)/delete', EventDelete.as_view(), name="event-delete")
)

