# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Song.page'
        db.delete_column('repertory_song', 'page')

        # Adding field 'Song.page'
        db.add_column('repertory_song', 'page',
                      self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True, null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Song.page'
        db.delete_column('repertory_song', 'page')

        # Adding field 'Song.page'
        db.add_column('repertory_song', 'page',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

    models = {
        'repertory.song': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Song'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'page': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'score_number': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
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
