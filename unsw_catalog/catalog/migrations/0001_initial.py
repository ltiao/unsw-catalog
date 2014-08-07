# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table(u'catalog_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('career', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('faculty', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('campus', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gened', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description_markup', self.gf('django.db.models.fields.TextField')()),
            ('uoc', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('eftsl', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=5)),
            ('accessed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('src_url', self.gf('django.db.models.fields.URLField')(max_length=80)),
        ))
        db.send_create_signal(u'catalog', ['Course'])

        # Adding unique constraint on 'Course', fields ['code', 'career', 'year']
        db.create_unique(u'catalog_course', ['code', 'career', 'year'])

        # Adding M2M table for field prereqs on 'Course'
        m2m_table_name = db.shorten_name(u'catalog_course_prereqs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_course', models.ForeignKey(orm[u'catalog.course'], null=False)),
            ('to_course', models.ForeignKey(orm[u'catalog.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_course_id', 'to_course_id'])

        # Adding M2M table for field exclusions on 'Course'
        m2m_table_name = db.shorten_name(u'catalog_course_exclusions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_course', models.ForeignKey(orm[u'catalog.course'], null=False)),
            ('to_course', models.ForeignKey(orm[u'catalog.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_course_id', 'to_course_id'])

        # Adding model 'Class'
        db.create_table(u'catalog_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(related_name='classes', to=orm['catalog.Course'])),
            ('class_nbr', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('activity', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('section', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('teaching', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('enrolments', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('capacity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('offering_start', self.gf('django.db.models.fields.DateField')()),
            ('offering_end', self.gf('django.db.models.fields.DateField')()),
            ('census_date', self.gf('django.db.models.fields.DateField')()),
            ('mode', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('consent', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('accessed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('src_url', self.gf('django.db.models.fields.URLField')(max_length=80)),
        ))
        db.send_create_signal(u'catalog', ['Class'])

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


    def backwards(self, orm):
        # Removing unique constraint on 'Course', fields ['code', 'career', 'year']
        db.delete_unique(u'catalog_course', ['code', 'career', 'year'])

        # Deleting model 'Course'
        db.delete_table(u'catalog_course')

        # Removing M2M table for field prereqs on 'Course'
        db.delete_table(db.shorten_name(u'catalog_course_prereqs'))

        # Removing M2M table for field exclusions on 'Course'
        db.delete_table(db.shorten_name(u'catalog_course_exclusions'))

        # Deleting model 'Class'
        db.delete_table(u'catalog_class')

        # Deleting model 'Meeting'
        db.delete_table(u'catalog_meeting')


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