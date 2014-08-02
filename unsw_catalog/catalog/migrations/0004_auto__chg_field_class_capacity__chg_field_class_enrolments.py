# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Class.capacity'
        db.alter_column(u'catalog_class', 'capacity', self.gf('django.db.models.fields.CharField')(max_length=5))

        # Changing field 'Class.enrolments'
        db.alter_column(u'catalog_class', 'enrolments', self.gf('django.db.models.fields.CharField')(max_length=5))

    def backwards(self, orm):

        # Changing field 'Class.capacity'
        db.alter_column(u'catalog_class', 'capacity', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'Class.enrolments'
        db.alter_column(u'catalog_class', 'enrolments', self.gf('django.db.models.fields.PositiveIntegerField')())

    models = {
        u'catalog.class': {
            'Meta': {'object_name': 'Class'},
            'accessed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'capacity': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'census_date': ('django.db.models.fields.DateField', [], {}),
            'class_nbr': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'consent': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'classes'", 'to': u"orm['catalog.Course']"}),
            'enrolments': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'offering_end': ('django.db.models.fields.DateField', [], {}),
            'offering_start': ('django.db.models.fields.DateField', [], {}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'src_url': ('django.db.models.fields.URLField', [], {'max_length': '80'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'teaching': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'catalog.course': {
            'Meta': {'unique_together': "(('code', 'career', 'year'),)", 'object_name': 'Course'},
            'accessed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'campus': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'career': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description_markup': ('django.db.models.fields.TextField', [], {}),
            'eftsl': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '5'}),
            'exclusions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'exclusions_rel_+'", 'to': u"orm['catalog.Course']"}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'gened': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'prereqs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalog.Course']", 'symmetrical': 'False'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'src_url': ('django.db.models.fields.URLField', [], {'max_length': '80'}),
            'uoc': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'catalog.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'classe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'meetings'", 'to': u"orm['catalog.Class']"}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_end': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'time_start': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'weeks': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['catalog']