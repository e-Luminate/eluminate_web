# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Day'
        db.create_table('events_day', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=9)),
        ))
        db.send_create_signal('events', ['Day'])

        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['participant.Participant'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('events', ['Event'])

        # Adding M2M table for field days on 'Event'
        db.create_table('events_event_days', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['events.event'], null=False)),
            ('day', models.ForeignKey(orm['events.day'], null=False))
        ))
        db.create_unique('events_event_days', ['event_id', 'day_id'])


    def backwards(self, orm):
        # Deleting model 'Day'
        db.delete_table('events_day')

        # Deleting model 'Event'
        db.delete_table('events_event')

        # Removing M2M table for field days on 'Event'
        db.delete_table('events_event_days')


    models = {
        'events.day': {
            'Meta': {'object_name': 'Day'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        },
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'days': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['events.Day']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['participant.Participant']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
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

    complete_apps = ['events']