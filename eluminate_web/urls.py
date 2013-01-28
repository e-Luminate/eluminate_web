from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),

    url(r'^participants/', include("participant.urls")),
    url(r'^sponsors/$', TemplateView.as_view(template_name="sponsors.html"), name="sponsors"),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name="contact"),
    url(r"^account/", include("account.urls")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^events/", include("events.urls")),  
    url(r'^maps/', include("maps.urls")),
    url(r'^profile/', include("participant_profile.urls")),
    url(r'^search/', include("search.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
