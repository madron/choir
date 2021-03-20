# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usage'
        db.create_table('repertory_usage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, db_index=True)),
        ))
        db.send_create_signal('repertory', ['Usage'])

        # Adding model 'Period'
        db.create_table('repertory_period', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200, db_index=True)),
        ))
        db.send_create_signal('repertory', ['Period'])

        # Adding field 'Song.period'
        db.add_column('repertory_song', 'period',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertory.Period'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Song.usage'
        db.add_column('repertory_song', 'usage',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertory.Usage'], null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting model 'Usage'
        db.delete_table('repertory_usage')

        # Deleting model 'Period'
        db.delete_table('repertory_period')

        # Deleting field 'Song.period'
        db.delete_column('repertory_song', 'period_id')

        # Deleting field 'Song.usage'
        db.delete_column('repertory_song', 'usage_id')

    models = {
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
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertory.Period']", 'null': 'True', 'blank': 'True'}),
            'score_number': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'tempo': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'usage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertory.Usage']", 'null': 'True', 'blank': 'True'})
        },
        'repertory.songfile': {
            'Meta': {'ordering': "('file',)", 'object_name': 'SongFile'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertory.Song']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'repertory.usage': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Usage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['repertory']