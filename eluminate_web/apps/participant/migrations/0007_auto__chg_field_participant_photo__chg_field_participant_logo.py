# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Participant.photo'
        db.alter_column('participant_participant', 'photo', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=200))

        # Changing field 'Participant.logo'
        db.alter_column('participant_participant', 'logo', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=200))

    def backwards(self, orm):

        # Changing field 'Participant.photo'
        db.alter_column('participant_participant', 'photo', self.gf('django.db.models.fields.files.ImageField')(max_length=200, null=True))

        # Changing field 'Participant.logo'
        db.alter_column('participant_participant', 'logo', self.gf('django.db.models.fields.files.ImageField')(max_length=200, null=True))

    models = {
        'participant.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'participant.participant': {
            'Meta': {'object_name': 'Participant'},
            'approved_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['participant.Category']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        }
    }

    complete_apps = ['participant']