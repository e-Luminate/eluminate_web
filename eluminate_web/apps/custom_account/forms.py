from django.forms import CharField, SlugField, ImageField, ModelMultipleChoiceField, \
                            Textarea

from account.forms import SignupForm
from participant.models import Category

class CustomSignupForm(SignupForm):
    participant_name = CharField(
    )
    participant_slug = SlugField(
        label = "Slug",
        help_text = "URL-safe version of above"
    )
    participant_website = CharField(
        label = "Website address (optional)",
        required = False, 
        initial = "http://"
    )
    participant_logo = ImageField(
        label = "Upload logo"
    )
    participant_photo = ImageField(
        label = "Upload a photo (optional)",
        required = False
    )
    participant_description = CharField(
        label = "Description",
        required = False, 
        widget = Textarea)
    participant_categories = ModelMultipleChoiceField(
        label = "Categories",
        help_text = "Select as many as apply using Ctrl key and mouse select",
        queryset = Category.objects.all()
    ) 
