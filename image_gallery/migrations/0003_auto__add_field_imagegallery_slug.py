# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ImageGallery.slug'
        db.add_column('image_gallery_imagegallery', 'slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ImageGallery.slug'
        db.delete_column('image_gallery_imagegallery', 'slug')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['image_gallery']
