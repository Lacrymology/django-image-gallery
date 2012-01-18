from django import template
from django.conf import settings

register = template.Library()

def image_gallery(context):
    gallery = context.get('gallery', None)
    return {
        'gallery': gallery,
        'media_url' : settings.MEDIA_URL,
        'context': context,
        }

register.inclusion_tag('image_gallery/gallery.html',
                       takes_context=True)(image_gallery)
