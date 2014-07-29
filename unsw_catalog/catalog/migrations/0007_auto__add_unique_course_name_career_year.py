# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Course', fields ['name', 'career', 'year']
        db.create_unique(u'catalog_course', ['name', 'career', 'year'])


    def backwards(self, orm):
        # Removing unique constraint on 'Course', fields ['name', 'career', 'year']
        db.delete_unique(u'catalog_course', ['name', 'career', 'year'])


    models = {
        u'catalog.class': {
            'Meta': {'object_name': 'Class'},
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'class_nbr': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'catalog.course': {
            'Meta': {'unique_together': "(('name', 'career', 'year'),)", 'object_name': 'Course'},
            'campus': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'career': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description_markup': ('django.db.models.fields.TextField', [], {}),
            'eftsl': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '5'}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'gened': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uoc': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '80'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['catalog']