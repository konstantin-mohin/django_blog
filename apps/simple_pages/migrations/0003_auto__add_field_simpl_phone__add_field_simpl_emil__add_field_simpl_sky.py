# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Simpl.phone'
        db.add_column('simple_pages_simpl', 'phone', self.gf('django.db.models.fields.CharField')(default=2, max_length=128), keep_default=False)

        # Adding field 'Simpl.emil'
        db.add_column('simple_pages_simpl', 'emil', self.gf('django.db.models.fields.CharField')(default=2, max_length=128), keep_default=False)

        # Adding field 'Simpl.skype'
        db.add_column('simple_pages_simpl', 'skype', self.gf('django.db.models.fields.CharField')(default=2, max_length=128), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Simpl.phone'
        db.delete_column('simple_pages_simpl', 'phone')

        # Deleting field 'Simpl.emil'
        db.delete_column('simple_pages_simpl', 'emil')

        # Deleting field 'Simpl.skype'
        db.delete_column('simple_pages_simpl', 'skype')


    models = {
        'simple_pages.simpl': {
            'Meta': {'object_name': 'Simpl'},
            'emil': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'main_banner': ('django.db.models.fields.CharField', [], {'max_length': '252', 'null': 'True', 'blank': 'True'}),
            'metades': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'metakey': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['simple_pages']
