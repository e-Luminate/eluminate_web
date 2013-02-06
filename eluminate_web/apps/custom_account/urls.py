from django.conf.urls import patterns, include, url

from custom_account.views import CustomSignupView

urlpatterns = patterns('',
    url(r'^signup/', CustomSignupView.as_view(), name="account_signup"),
    url(r"^", include("account.urls")),
)
