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

class EventSearchManager(models.Manager):
    def searched(self, term):
        return Event.objects.filter(name__icontains=term)

class Event(models.Model):
    name = models.CharField(max_length = 256, help_text="The name of the event")
    start_time = models.TimeField(help_text="When it starts, e.g. 12:00")
    end_time = models.TimeField(help_text="When the event finish, e.g. 16:00")
    days = models.ManyToManyField(Day)
    participant = models.ForeignKey(Participant)
    description = models.TextField()
    location = models.ForeignKey(Location, null=True)
    searched_objects = EventSearchManager()
    objects = models.Manager()
    
    def get_absolute_url(self):
        return(reverse("event-detail", args=[self.id]))
    
    def __str__(self):
        return self.name 
