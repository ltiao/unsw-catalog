# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Meeting'
        db.create_table(u'catalog_meeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classe', self.gf('django.db.models.fields.related.ForeignKey')(related_name='meetings', to=orm['catalog.Class'])),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('time_start', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('time_end', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('weeks', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('instructor', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'catalog', ['Meeting'])

        # Adding field 'Class.teaching'
        db.add_column(u'catalog_class', 'teaching',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Class.status'
        db.add_column(u'catalog_class', 'status',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Adding field 'Class.enrolments'
        db.add_column(u'catalog_class', 'enrolments',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Class.capacity'
        db.add_column(u'catalog_class', 'capacity',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Class.offering_start'
        db.add_column(u'catalog_class', 'offering_start',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime.today()),
                      keep_default=False)

        # Adding field 'Class.offering_end'
        db.add_column(u'catalog_class', 'offering_end',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime.today()),
                      keep_default=False)

        # Adding field 'Class.census_date'
        db.add_column(u'catalog_class', 'census_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime.today()),
                      keep_default=False)

        # Adding field 'Class.mode'
        db.add_column(u'catalog_class', 'mode',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'Class.consent'
        db.add_column(u'catalog_class', 'consent',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding unique constraint on 'Class', fields ['class_nbr']
        db.create_unique(u'catalog_class', ['class_nbr'])


    def backwards(self, orm):
        # Removing unique constraint on 'Class', fields ['class_nbr']
        db.delete_unique(u'catalog_class', ['class_nbr'])

        # Deleting model 'Meeting'
        db.delete_table(u'catalog_meeting')

        # Deleting field 'Class.teaching'
        db.delete_column(u'catalog_class', 'teaching')

        # Deleting field 'Class.status'
        db.delete_column(u'catalog_class', 'status')

        # Deleting field 'Class.enrolments'
        db.delete_column(u'catalog_class', 'enrolments')

        # Deleting field 'Class.capacity'
        db.delete_column(u'catalog_class', 'capacity')

        # Deleting field 'Class.offering_start'
        db.delete_column(u'catalog_class', 'offering_start')

        # Deleting field 'Class.offering_end'
        db.delete_column(u'catalog_class', 'offering_end')

        # Deleting field 'Class.census_date'
        db.delete_column(u'catalog_class', 'census_date')

        # Deleting field 'Class.mode'
        db.delete_column(u'catalog_class', 'mode')

        # Deleting field 'Class.consent'
        db.delete_column(u'catalog_class', 'consent')


    models = {
        u'catalog.class': {
            'Meta': {'object_name': 'Class'},
            'accessed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'capacity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'census_date': ('django.db.models.fields.DateField', [], {}),
            'class_nbr': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'consent': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'classes'", 'to': u"orm['catalog.Course']"}),
            'enrolments': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'offering_end': ('django.db.models.fields.DateField', [], {}),
            'offering_start': ('django.db.models.fields.DateField', [], {}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'teaching': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '80'})
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
            'uoc': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '80'}),
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