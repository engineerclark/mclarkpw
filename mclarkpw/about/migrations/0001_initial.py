# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('about_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('about', ['Tag'])

        # Adding model 'Position'
        db.create_table('about_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('about', ['Position'])

        # Adding M2M table for field tags on 'Position'
        m2m_table_name = db.shorten_name('about_position_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('position', models.ForeignKey(orm['about.position'], null=False)),
            ('tag', models.ForeignKey(orm['about.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['position_id', 'tag_id'])

        # Adding model 'School'
        db.create_table('about_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('program', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('about', ['School'])

        # Adding M2M table for field tags on 'School'
        m2m_table_name = db.shorten_name('about_school_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('school', models.ForeignKey(orm['about.school'], null=False)),
            ('tag', models.ForeignKey(orm['about.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['school_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('about_tag')

        # Deleting model 'Position'
        db.delete_table('about_position')

        # Removing M2M table for field tags on 'Position'
        db.delete_table(db.shorten_name('about_position_tags'))

        # Deleting model 'School'
        db.delete_table('about_school')

        # Removing M2M table for field tags on 'School'
        db.delete_table(db.shorten_name('about_school_tags'))


    models = {
        'about.position': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Position'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['about.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'about.school': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'School'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['about.Tag']", 'symmetrical': 'False'})
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