# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Position.hide'
        db.add_column('about_position', 'hide',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'School.hide'
        db.add_column('about_school', 'hide',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Position.hide'
        db.delete_column('about_position', 'hide')

        # Deleting field 'School.hide'
        db.delete_column('about_school', 'hide')


    models = {
        'about.position': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Position'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hide': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['about.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'about.school': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'School'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hide': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['about.Tag']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'about.tag': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Tag'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['about']