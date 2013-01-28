from django.core.urlresolvers import reverse
from django.db import models

class Category(models.Model):
    name = models.CharField(unique=True, max_length=20, help_text=u'Cleantech category')   

    class Meta:
        verbose_name_plural = u'Categories'

    def __unicode__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=255, help_text=u'Name of participating company')
    slug = models.SlugField(max_length=255, unique=True, help_text=u'Unique URL-safe version of name')
    website = models.CharField(max_length=2000, help_text=u'Website URL')
    logo = models.ImageField(upload_to='participant_logos/%Y/%m/%d', max_length=200, null=True, help_text=u'Company logo')
    photo = models.ImageField(upload_to='participant_photos/%Y/%m/%d', max_length=200, null=True, help_text=u'Company photo')
    description = models.TextField(blank=True, help_text=u'Description of the participating company')
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True, help_text=u'Date/Time when company was first created')
    approved_on = models.DateTimeField(null=True, blank=True, help_text=u'Date/Time when company was approved to appear online')

    def __unicode__(self):
        return self.name

    def approved(self):
        return self.approved_on != None

    def get_absolute_url(self):
        return reverse('participant_detail', kwargs={'slug': self.slug})
