from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r'^maps/', include("maps.urls")),
    
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
