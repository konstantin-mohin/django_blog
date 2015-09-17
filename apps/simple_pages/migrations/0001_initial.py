# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Simpl'
        db.create_table('simple_pages_simpl', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('simple_pages', ['Simpl'])


    def backwards(self, orm):
        
        # Deleting model 'Simpl'
        db.delete_table('simple_pages_simpl')


    models = {
        'simple_pages.simpl': {
            'Meta': {'object_name': 'Simpl'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['simple_pages']
