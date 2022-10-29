from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from utils.unique_slug_generator import unique_slug_generator

from datetime import datetime

class Taxonomy(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(_('title'), max_length=350)
    description = RichTextUploadingField(_('description'), blank=True, null=True)
    slug = models.SlugField(_('slug'), unique=True, blank=True)
    thumbnail = models.ImageField(_('thumbnail'), upload_to=f'taxonomy/thumbnails/{str(datetime.now().year)}/{str(datetime.now().month)}', blank=True, null=True)
    thumbnail_alt = models.CharField(_('thumbnail alt'), max_length=350, blank=True)


@receiver(pre_save, sender=Taxonomy)
def taxonomy_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = instance.title
