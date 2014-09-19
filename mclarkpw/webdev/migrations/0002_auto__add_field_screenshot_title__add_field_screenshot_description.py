# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Screenshot.title'
        db.add_column('webdev_screenshot', 'title',
                      self.gf('django.db.models.fields.CharField')(default='Screenshot', max_length=128),
                      keep_default=False)

        # Adding field 'Screenshot.description'
        db.add_column('webdev_screenshot', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Screenshot.title'
        db.delete_column('webdev_screenshot', 'title')

        # Deleting field 'Screenshot.description'
        db.delete_column('webdev_screenshot', 'description')


    models = {
        'about.tag': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Tag'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'webdev.project': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['about.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'webdev.screenshot': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Screenshot'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['webdev.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Screenshot'", 'max_length': '128'})
        }
    }

    complete_apps = ['webdev']