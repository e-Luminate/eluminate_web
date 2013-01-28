from django.conf.urls import patterns, url

from participant.views import ParticipantLandingView, ParticipantDetailView

urlpatterns = patterns('participant.views',
    url(r'^$', ParticipantLandingView.as_view(), name='participant_landing'),
    url(r'^detail/(?P<slug>[a-z0-9]+)/$', ParticipantDetailView.as_view(), name='participant_detail'),
)
