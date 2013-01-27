from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Field
from crispy_forms.bootstrap import FormActions
from django.forms import ModelForm
from models import Location
from widgets import LeafletMapWidget

class LocationForm(ModelForm):

    class Meta:
        model = Location
        fields = ('name',
                   'marker'
                   )
        widgets = {
            'marker': LeafletMapWidget,
        }
 
    
    def __init__(self, user=None, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'saveLocation'
        self.helper.form_class = '' 
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        #self.helper.help_text_inline = True
        self.helper.layout = Layout(
                Field('name', css_class="span9"),
                Field('marker'),
                               )
        self.user = user
        super(LocationForm, self).__init__(*args, **kwargs)

class AddLocationForm(LocationForm):
    def __init__(self, *args, **kwargs):
        super(AddLocationForm, self).__init__(*args, **kwargs)
        self.helper.form_action = 'add_location'
        self.helper.layout.fields.append(
           FormActions(
               Reset('reset','Reset'),
               Submit('submit', 'Add Location', css_class="btn-primary")
           )
        )
        
    
class EditLocationForm(LocationForm):
    def __init__(self, *args, **kwargs):
        super(EditLocationForm, self).__init__(*args, **kwargs)
        self.helper.form_action = '' #Got it from the location instance
        self.helper.layout.fields.append(
           FormActions(
               Reset('reset','Reset'),
               Submit('submit', 'Edit Location', css_class="btn-primary")
           )
        )
    
