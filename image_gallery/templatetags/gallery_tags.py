"""
Template tags for image-gallery.

 * image_gallery renders the gallery template
"""
from django import template

register = template.Library()

def image_gallery(context):
    """
    Renders the template image_gallery/gallery.html passing it the
    following variables:
      * gallery: the current `gallery` context variable, which is the gallery
         to be rendered
      * context: the parent context, in case anything is needed from it

    TODO: pass the gallery as a parameter
    """
    gallery = context.get('gallery', None)
    return {
        'gallery': gallery,
        'context': context,
        }

register.inclusion_tag('image_gallery/gallery.html',
                       takes_context=True)(image_gallery)
