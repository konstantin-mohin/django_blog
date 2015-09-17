# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Simpl.title'
        db.add_column('simple_pages_simpl', 'title', self.gf('django.db.models.fields.CharField')(default=2, max_length=128), keep_default=False)

        # Adding field 'Simpl.logo'
        db.add_column('simple_pages_simpl', 'logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Simpl.main_banner'
        db.add_column('simple_pages_simpl', 'main_banner', self.gf('django.db.models.fields.CharField')(max_length=252, null=True, blank=True), keep_default=False)

        # Adding field 'Simpl.metakey'
        db.add_column('simple_pages_simpl', 'metakey', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Simpl.metades'
        db.add_column('simple_pages_simpl', 'metades', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Simpl.title'
        db.delete_column('simple_pages_simpl', 'title')

        # Deleting field 'Simpl.logo'
        db.delete_column('simple_pages_simpl', 'logo')

        # Deleting field 'Simpl.main_banner'
        db.delete_column('simple_pages_simpl', 'main_banner')

        # Deleting field 'Simpl.metakey'
        db.delete_column('simple_pages_simpl', 'metakey')

        # Deleting field 'Simpl.metades'
        db.delete_column('simple_pages_simpl', 'metades')


    models = {
        'simple_pages.simpl': {
            'Meta': {'object_name': 'Simpl'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'main_banner': ('django.db.models.fields.CharField', [], {'max_length': '252', 'null': 'True', 'blank': 'True'}),
            'metades': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'metakey': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['simple_pages']
