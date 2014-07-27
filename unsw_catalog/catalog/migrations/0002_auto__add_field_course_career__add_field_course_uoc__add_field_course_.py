# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Course.career'
        db.add_column(u'catalog_course', 'career',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=15),
                      keep_default=False)

        # Adding field 'Course.uoc'
        db.add_column(u'catalog_course', 'uoc',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=6),
                      keep_default=False)

        # Adding field 'Course.faculty'
        db.add_column(u'catalog_course', 'faculty',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=25),
                      keep_default=False)

        # Adding field 'Course.school'
        db.add_column(u'catalog_course', 'school',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=25),
                      keep_default=False)

        # Adding field 'Course.campus'
        db.add_column(u'catalog_course', 'campus',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=20),
                      keep_default=False)

        # Adding field 'Course.eftsl'
        db.add_column(u'catalog_course', 'eftsl',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=5),
                      keep_default=False)


        # Changing field 'Course.name'
        db.alter_column(u'catalog_course', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Deleting field 'Course.career'
        db.delete_column(u'catalog_course', 'career')

        # Deleting field 'Course.uoc'
        db.delete_column(u'catalog_course', 'uoc')

        # Deleting field 'Course.faculty'
        db.delete_column(u'catalog_course', 'faculty')

        # Deleting field 'Course.school'
        db.delete_column(u'catalog_course', 'school')

        # Deleting field 'Course.campus'
        db.delete_column(u'catalog_course', 'campus')

        # Deleting field 'Course.eftsl'
        db.delete_column(u'catalog_course', 'eftsl')


        # Changing field 'Course.name'
        db.alter_column(u'catalog_course', 'name', self.gf('django.db.models.fields.CharField')(max_length=25))

    models = {
        u'catalog.course': {
            'Meta': {'object_name': 'Course'},
            'campus': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'career': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'eftsl': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '5'}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'gened': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'uoc': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['catalog']