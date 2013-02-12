from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from account.views import SignupView, ConfirmEmailView

from custom_account.forms import CustomSignupForm
from participant.models import Participant

class CustomSignupView(SignupView):

    form_class = CustomSignupForm

    def after_signup(self, form):
        self.create_participant(form)
        super(CustomSignupView, self).after_signup(form)

    def create_participant(self, form):
        participant = Participant(
            user = self.created_user,
            name = form.cleaned_data.get("participant_name"),
            slug = form.cleaned_data.get("participant_slug"),
            website = form.cleaned_data.get("participant_website"),
            logo = form.cleaned_data.get("participant_logo"),
            photo = form.cleaned_data.get("participant_photo"),
            description = form.cleaned_data.get("participant_description")
        )
        participant.save()
        for category in form.cleaned_data.get("participant_categories"):
            participant.categories.add(category)
        participant.save()


class CustomConfirmEmailView(ConfirmEmailView):

    ConfirmEmailView.messages["email_confirmed"]["text"] = _("You have confirmed %(email)s for user account %(username)s")
    
    def post(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm()
        user = confirmation.email_address.user
        user.is_active = True
        user.save()
        redirect_url = self.get_redirect_url()
        if not redirect_url:
            ctx = self.get_context_data()
            return self.render_to_response(ctx)
        if self.messages.get("email_confirmed"):
            messages.add_message(
                self.request,
                self.messages["email_confirmed"]["level"],
                self.messages["email_confirmed"]["text"] % {
                    "email": confirmation.email_address.email,
                    "username": confirmation.email_address.user.username
                }
            )
        return redirect("%s?next=%s" % (reverse(redirect_url), reverse('events-list-user')))
