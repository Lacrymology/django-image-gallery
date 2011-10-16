# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ImageGallery'
        db.create_table('image_gallery_imagegallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('image_gallery', ['ImageGallery'])

        # Adding model 'Image'
        db.create_table('image_gallery_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inline_ordering_position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['image_gallery.ImageGallery'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('src_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('src_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
        ))
        db.send_create_signal('image_gallery', ['Image'])


    def backwards(self, orm):
        
        # Deleting model 'ImageGallery'
        db.delete_table('image_gallery_imagegallery')

        # Deleting model 'Image'
        db.delete_table('image_gallery_image')


    models = {
        'image_gallery.image': {
            'Meta': {'ordering': "('inline_ordering_position',)", 'object_name': 'Image'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_gallery.ImageGallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'inline_ordering_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'src_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'src_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'})
        },
        'image_gallery.imagegallery': {
            'Meta': {'object_name': 'ImageGallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['image_gallery']
