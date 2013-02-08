from account.views import SignupView

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
