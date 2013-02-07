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
            name = form.cleaned_data.get("name"),
            slug = form.cleaned_data.get("slug"),
            website = form.cleaned_data.get("website"),
            logo = form.cleaned_data.get("logo"),
            photo = form.cleaned_data.get("photo"),
            description = form.cleaned_data.get("description")
        )
        participant.save()
        for category in form.cleaned_data.get("categories"):
            participant.categories.add(category)
        participant.save()
