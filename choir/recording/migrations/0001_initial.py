# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RecordingSong'
        db.create_table('recording_recordingsong', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('importance', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('song', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['repertory.Song'], unique=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('recording', ['RecordingSong'])

        # Adding model 'RecordingSongPart'
        db.create_table('recording_recordingsongpart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recording_song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recording.RecordingSong'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('recording', ['RecordingSongPart'])


    def backwards(self, orm):
        # Deleting model 'RecordingSong'
        db.delete_table('recording_recordingsong')

        # Deleting model 'RecordingSongPart'
        db.delete_table('recording_recordingsongpart')


    models = {
        'recording.recordingsong': {
            'Meta': {'ordering': "('completed', '-importance', 'song__name')", 'object_name': 'RecordingSong'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'song': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['repertory.Song']", 'unique': 'True'})
        },
        'recording.recordingsongpart': {
            'Meta': {'ordering': "('order',)", 'object_name': 'RecordingSongPart'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recording_song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recording.RecordingSong']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_changed': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
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

    complete_apps = ['recording']