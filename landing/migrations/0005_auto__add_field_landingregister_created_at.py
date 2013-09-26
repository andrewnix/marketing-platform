# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LandingRegister.created_at'
        db.add_column(u'landing_landingregister', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 8, 16, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LandingRegister.created_at'
        db.delete_column(u'landing_landingregister', 'created_at')


    models = {
        u'landing.formtext': {
            'Meta': {'object_name': 'FormText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'landing.function': {
            'Meta': {'object_name': 'Function'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'landing.landingregister': {
            'Meta': {'object_name': 'LandingRegister'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '600', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'was_contacted': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'landing.mainimage': {
            'Description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'MainImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'landing.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'landing.slogan': {
            'Meta': {'object_name': 'Slogan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'landing.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['landing']