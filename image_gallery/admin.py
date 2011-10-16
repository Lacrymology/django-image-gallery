from django.contrib import admin
from inline_ordering.admin import OrderableStackedInline
from image_gallery.models import ImageGallery, Image

class ImageInline(OrderableStackedInline):
    model = Image

class ImageGalleryAdmin(admin.ModelAdmin):
    """
    Admin manager for the ImageGallery model
    """
    model = ImageGallery
    inlines = (ImageInline,)
    prepopulated_fields = { "slug": ("name",) }

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1/jquery-ui.min.js',
            )

admin.site.register(ImageGallery, ImageGalleryAdmin)
