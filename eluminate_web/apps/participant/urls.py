from django.conf.urls import patterns, url

from participant.views import ParticipantLandingView

urlpatterns = patterns('participant.views',
    url(r'^$', ParticipantLandingView.as_view(), name='participant_landing'),
)
