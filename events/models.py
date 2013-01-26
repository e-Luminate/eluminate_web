from django.db import models

class Event(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    
class Day(models.Model):
    name = models.CharField(max_length = 9)
    events = models.ManyToManyField(Event)

