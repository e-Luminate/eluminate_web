from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ("name", 
                  "start_time",
                  "end_time",
                  "days",
                  "description")