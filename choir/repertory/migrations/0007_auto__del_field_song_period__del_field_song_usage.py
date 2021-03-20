# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Song.period'
        db.delete_column('repertory_song', 'period_id')

        # Deleting field 'Song.usage'
        db.delete_column('repertory_song', 'usage_id')

        # Adding M2M table for field periods on 'Song'
        db.create_table('repertory_song_periods', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('song', models.ForeignKey(orm['repertory.song'], null=False)),
            ('period', models.ForeignKey(orm['repertory.period'], null=False))
        ))
        db.create_unique('repertory_song_periods', ['song_id', 'period_id'])

        # Adding M2M table for field usages on 'Song'
        db.create_table('repertory_song_usages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('song', models.ForeignKey(orm['repertory.song'], null=False)),
            ('usage', models.ForeignKey(orm['repertory.usage'], null=False))
        ))
        db.create_unique('repertory_song_usages', ['song_id', 'usage_id'])


    def backwards(self, orm):
        # Adding field 'Song.period'
        db.add_column('repertory_song', 'period',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertory.Period'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Song.usage'
        db.add_column('repertory_song', 'usage',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertory.Usage'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field periods on 'Song'
        db.delete_table('repertory_song_periods')

        # Removing M2M table for field usages on 'Song'
        db.delete_table('repertory_song_usages')


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