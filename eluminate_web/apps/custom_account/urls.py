from django.conf.urls import patterns, include, url

from custom_account.views import CustomSignupView, CustomConfirmEmailView

urlpatterns = patterns('',
    url(r'^signup/', CustomSignupView.as_view(), name="account_signup"),
    url(r"^confirm_email/(?P<key>\w+)/$", CustomConfirmEmailView.as_view(), name="account_confirm_email"),
    url(r"^", include("account.urls")),
)
