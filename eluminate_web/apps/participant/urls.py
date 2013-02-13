from django.conf.urls import patterns, url

from .views import ParticipantLandingView, ParticipantDetailView, ParticipantFilterRedirectView, \
                   ParticipantCreateView, ParticipantUpdateView, ParticipantDeleteView


urlpatterns = patterns('participant.views',
    url(r'^$', ParticipantLandingView.as_view(), name='participant_landing'),
    url(r'^create$', ParticipantCreateView.as_view(), name="participant_create"),
    url(r'^filter/$', ParticipantFilterRedirectView.as_view(), name='participant_filter'),
    url(r'^(?P<slug>[a-z0-9_\-]+)/$', ParticipantDetailView.as_view(), name='participant_detail'),
    url(r'^(?P<slug>[a-z0-9_\-]+)/update/$', ParticipantUpdateView.as_view(), name="participant_update"),
    url(r'^(?P<slug>[a-z0-9_\-]+)/delete/$', ParticipantDeleteView.as_view(), name="participant_delete")
)
