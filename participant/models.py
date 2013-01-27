from django.db import models

class Participant(models.Model):
   name = models.CharField(max_length=255, help_text=u'Name of participating company')
   slug = models.SlugField(max_length=255, unique=True, help_text=u'Unique URL-safe version of name')
   website = models.CharField(max_length=2000, help_text=u'Website URL')
   #logo = models.ImageField()
   description = models.TextField(blank=True, help_text=u'Description of the participating company')
   created = models.DateTimeField(auto_now_add=True, help_text=u'Date/Time when company was first created')
   approved_on = models.DateTimeField(null=True, blank=True, help_text=u'Date/Time when company was approved to appear online')

   def __unicode__(self):
       return self.name

   def approved(self):
       return self.approved_on != None
