from django.db import models
from django.core.urlresolvers import reverse
from django import forms

from south.modelsinspector import add_introspection_rules

from participant.models import Participant
from maps.models import Location

class Day(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        
        return self.name

class Event(models.Model):
    name = models.CharField(max_length = 256)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days = models.ManyToManyField(Day)
    participant = models.ForeignKey(Participant)
    description = models.TextField()
    location = models.ForeignKey(Location, null=True)
    
    
    def get_absolute_url(self):
        return(reverse("event-detail", args=[self.id]))
    
    def __str__(self):
        return self.name 
