from django.db import models

class Day(models.Model):
    name = models.CharField(max_length = 9)

class Event(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    days = models.ManyToManyField(Day)

