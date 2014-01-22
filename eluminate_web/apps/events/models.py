from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
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
    participant = models.ForeignKey(Participant, related_name="own_events")
    collaborators = models.ManyToManyField(Participant, related_name="collaboration_events", 
                                           blank=True, null=True)
    photo = models.ImageField(upload_to='event_photos/%Y/%m/%d', max_length=200, blank=True, help_text=u'Event photo', default='')
    description = models.TextField()
    location = models.ForeignKey(Location, null=True)
    searched_objects = EventSearchManager()
    objects = models.GeoManager()

    def save(self, *args, **kwargs):
        if self.id and self.participant in self.collaborators.all():
            raise forms.ValidationError("Participant '%s' is a collaborator - can't be the owner too" % self.participant)
        else:
            super(Event, self).save()
    
    def get_absolute_url(self):
        return(reverse("event-detail", args=[self.id]))
    
    def __str__(self):
        return self.name

    def approved_collaborators(self):
        return self.collaborators.exclude(approved_on=None)

@receiver(m2m_changed, sender=Event.collaborators.through)
def collaborators_changed(sender, instance, action, pk_set, **kwargs):
    if action == "pre_add":
        if instance.participant.id in pk_set:
            raise forms.ValidationError("Participant '%s' is the owner - can't be a collaborator too" % instance.participant)
