from django.forms import CharField, SlugField, ImageField, ModelMultipleChoiceField, \
                            Textarea

from account.forms import SignupForm
from participant.models import Category

class CustomSignupForm(SignupForm):
    name = CharField(
        label = "Participant Name",
        help_text = "Name of company or organization you represent"
    )
    slug = SlugField(
        label = "Slug",
        help_text = "URL-safe version of above"
    )
    website = CharField(
        label = "Website address (optional)",
        required = False, 
        initial = "http://"
    )
    logo = ImageField(
        label = "Upload logo"
    )
    photo = ImageField(
        label = "Upload a photo (optional)",
        required = False
    )
    description = CharField(
        label = "Description",
        help_text = "Description of company or organization you represent",
        required = False, 
        widget = Textarea)
    categories = ModelMultipleChoiceField(
        label = "Categories",
        help_text = "Select as many as apply using Ctrl key and mouse select",
        queryset = Category.objects.all()
    ) 
