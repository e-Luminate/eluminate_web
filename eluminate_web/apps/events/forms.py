from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Field, Div, HTML
from crispy_forms.bootstrap import FormActions

from .models import Event


class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ("name", 
                  "start_time",
                  "end_time",
                  "days",
                  "location",
                  "description")
        widgets = {
                   'days' : CheckboxSelectMultiple
                   }
        
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'saveLocation'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.help_text_inline = True
        self.helper.layout = Layout(
            Div(Field('location', template="events/_location_form_field.html",),
                Field('name'),
                Field("start_time"),
                Field("end_time"),
                Field("days"),
                Field("description"),
                FormActions(
                            Submit('submit', 'Save', css_class="btn btn-primary")
                            )
                )
            )
        
        super(EventForm, self).__init__(*args, **kwargs)

        # Overriding the help text due to a django bug:
        # https://code.djangoproject.com/ticket/9321
        self.fields['days'].help_text = ''
        
        # This is another dirty hack, we should report to django.
        # The initial from a FormClass initial on a ModelChoiceField
        # does not get retained, so we override
#        import ipdb; ipdb.set_trace()
        if kwargs['initial'].has_key('location'):
            location_queryset = kwargs['initial']['location']
            self.fields['location'].queryset = location_queryset
            if self.instance:
                #import ipdb; ipdb.set_trace()
                location_selected = location_queryset.filter(id=self.instance.location.id)
                self.fields['location'].queryset=location_queryset
                self.fields['location'].initial = location_selected
                print self.instance.location
                                                  
                
 
                
        