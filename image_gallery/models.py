from django.db import models
from django.utils.translation import ugettext_lazy as _
from inline_ordering.models import Orderable

class ImageGallery(models.Model):
    """
    Gallery Model
    """
    name = models.CharField(max_length=64)
    slug = models.SlugField()
    
    class Meta:
        verbose_name_plural = "galleries"

    def __unicode__(self):
        return self.name

class Image(Orderable):
    """
    Image model for the gallery
    """
    def get_gallery_path(self, filename):
        """
        Get upload path depending on gallery name
        """
        return "%s/%s" % (self.gallery.slug, filename)

    gallery = models.ForeignKey(ImageGallery)
    image = models.ImageField(upload_to=get_gallery_path,
                              height_field='src_height',
                              width_field='src_width')
    src_height = models.PositiveSmallIntegerField(editable=False, null=True)
    src_width = models.PositiveSmallIntegerField(editable=False, null=True)

    text = models.CharField(max_length=127, blank=True,
                            help_text = _("Image text. Can be used as alt, or "
                                          "footnote, or whatever you want"))

    def __unicode__(self):
        return self.text or str(self.pk)
