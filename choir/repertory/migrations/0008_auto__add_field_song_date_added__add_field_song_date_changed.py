# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Song.date_added'
        db.add_column('repertory_song', 'date_added',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'Song.date_changed'
        db.add_column('repertory_song', 'date_changed',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, db_index=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Song.date_added'
        db.delete_column('repertory_song', 'date_added')

        # Deleting field 'Song.date_changed'
        db.delete_column('repertory_song', 'date_changed')


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