# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Song.tempo'
        db.add_column('repertory_song', 'tempo',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Song.composer'
        db.add_column('repertory_song', 'composer',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Song.lyrics_writer'
        db.add_column('repertory_song', 'lyrics_writer',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Song.tempo'
        db.delete_column('repertory_song', 'tempo')

        # Deleting field 'Song.composer'
        db.delete_column('repertory_song', 'composer')

        # Deleting field 'Song.lyrics_writer'
        db.delete_column('repertory_song', 'lyrics_writer')

    models = {
        'repertory.song': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Song'},
            'chords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'composer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lyrics_writer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'page': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'score_number': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'tempo': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'repertory.songfile': {
            'Meta': {'ordering': "('file',)", 'object_name': 'SongFile'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertory.Song']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['repertory']