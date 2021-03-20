# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(db_index=True, null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertory.Period'], null=True, blank=True)),
        ))
        db.send_create_signal('events', ['Event'])

        # Adding model 'EventSong'
        db.create_table('events_eventsong', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('usage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertory.Usage'], null=True, blank=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertory.Song'])),
            ('soloist', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('guide', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('events', ['EventSong'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('events_event')

        # Deleting model 'EventSong'
        db.delete_table('events_eventsong')


    models = {
        'events.event': {
            'Meta': {'ordering': "('-date', '-time', '-id')", 'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertory.Period']", 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'songs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['repertory.Song']", 'null': 'True', 'through': "orm['events.EventSong']", 'blank': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'events.eventsong': {
            'Meta': {'ordering': "('-event__date', '-event__time', '-event__id', 'order')", 'object_name': 'EventSong'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Event']"}),
            'guide': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'soloist': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertory.Song']"}),
            'usage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertory.Usage']", 'null': 'True', 'blank': 'True'})
        },
        'repertory.period': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Period'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'})
        },
        'repertory.song': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Song'},
            'chords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'composer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lyrics_writer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'page': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'periods': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['repertory.Period']", 'null': 'True', 'blank': 'True'}),
            'score_number': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'tempo': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'usages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['repertory.Usage']", 'null': 'True', 'blank': 'True'})
        },
        'repertory.usage': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Usage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['events']