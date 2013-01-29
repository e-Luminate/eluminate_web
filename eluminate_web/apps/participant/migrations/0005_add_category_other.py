# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        Category = orm['participant.Category']
        other_cat = Category(name='Other')
        other_cat.save()

    def backwards(self, orm):
        Category = orm['participant.Category']
        other_cat = Category.objects.get(name='Other')
        other_cat.delete()

    models = {
        'participant.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'participant.participant': {
            'Meta': {'object_name': 'Participant'},
            'approved_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        }
    }

    complete_apps = ['participant']
    symmetrical = True
