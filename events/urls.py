from django.conf.urls import patterns, url
from events import views

urlpatterns = patterns('',
    url(r'^$', events.index, name = 'index'),
    url(r'^(?P<event_id>\d+/$', events.show, name = 'show'),
)

