from django.conf.urls import patterns, url

from participant.views import ParticipantLandingView, \
                                ParticipantDetailView, \
                                ParticipantFilterRedirectView

urlpatterns = patterns('participant.views',
    url(r'^$', ParticipantLandingView.as_view(), name='participant_landing'),
    url(r'^detail/(?P<slug>[a-z0-9_\-]+)/$', ParticipantDetailView.as_view(), name='participant_detail'),
    url(r'^filter/$', ParticipantFilterRedirectView.as_view(), name='participant_filter'),
)
