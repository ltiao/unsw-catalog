# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Class'
        db.create_table(u'catalog_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Course'])),
            ('class_nbr', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('activity', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'catalog', ['Class'])


    def backwards(self, orm):
        # Deleting model 'Class'
        db.delete_table(u'catalog_class')


    models = {
        u'catalog.class': {
            'Meta': {'object_name': 'Class'},
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'class_nbr': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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