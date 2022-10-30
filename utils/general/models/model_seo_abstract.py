from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Seo(models.Model):
    class Meta:
        abstract = True

    meta_title = models.CharField(_('meta title'), max_length=320, blank=True, null=True)
    meta_description = RichTextUploadingField(_('meta description'), blank=True, null=True)



