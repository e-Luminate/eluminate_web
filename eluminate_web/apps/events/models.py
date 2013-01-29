from django.db import models
from participant.models import Participant

from django.db import models
from django import forms
from south.modelsinspector import add_introspection_rules


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
