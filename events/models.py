from django.db import models
from participant.models import Participant

class Day(models.Model):
    name = models.CharField(max_length = 9)

class Event(models.Model):
    name = models.CharField(max_length = 256)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days = models.ManyToManyField(Day)
    participant = models.ForeignKey(Participant)
    description = models.TextField()
