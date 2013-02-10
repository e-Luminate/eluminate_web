from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Field, Div, HTML, Fieldset
from crispy_forms.bootstrap import FormActions

from .models import Participant


class ParticipantForm(forms.ModelForm):
    
    class Meta:
        model = Participant
        fields = ("name", 
                  "slug",
                  "website",
                  "logo",
                  "photo",
                  "description", 
                  "categories",
                  )
        
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.help_text_inline = True
        self.helper.layout = Layout(
                
                Field("name"),
                Field("slug"),
                Field("website"),
                Field("logo"),
                Field("photo"),
                Field("description"),
                Field("categories"),                
                FormActions(
                            Submit('submit', 'Save', css_class="btn btn-primary")
                            )
                )
        super(ParticipantForm, self).__init__(*args, **kwargs)
