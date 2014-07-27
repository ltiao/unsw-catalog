# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Course.description'
        db.delete_column(u'catalog_course', 'description')

        # Adding field 'Course.description_markup'
        db.add_column(u'catalog_course', 'description_markup',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


        # Changing field 'Course.school'
        db.alter_column(u'catalog_course', 'school', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Course.name'
        db.alter_column(u'catalog_course', 'name', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Course.faculty'
        db.alter_column(u'catalog_course', 'faculty', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Course.campus'
        db.alter_column(u'catalog_course', 'campus', self.gf('django.db.models.fields.CharField')(max_length=25))

    def backwards(self, orm):
        # Adding field 'Course.description'
        db.add_column(u'catalog_course', 'description',
                      self.gf('django.db.models.fields.TextField')(default=0),
                      keep_default=False)

        # Deleting field 'Course.description_markup'
        db.delete_column(u'catalog_course', 'description_markup')


        # Changing field 'Course.school'
        db.alter_column(u'catalog_course', 'school', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'Course.name'
        db.alter_column(u'catalog_course', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Course.faculty'
        db.alter_column(u'catalog_course', 'faculty', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'Course.campus'
        db.alter_column(u'catalog_course', 'campus', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'catalog.course': {
            'Meta': {'object_name': 'Course'},
            'campus': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'career': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description_markup': ('django.db.models.fields.TextField', [], {}),
            'eftsl': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '5'}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'gened': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'uoc': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['catalog']