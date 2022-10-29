from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model

from utils.utile.unique_slug_generator import unique_slug_generator

from datetime import datetime


class BasicPost(models.Model):
    """
    This Class is for Posts.
    It's very important to know that, in author we use classname_posts related name.
    
    For Example if want to find all of user posts (Class name = Blog) we should use this:
    
    get_user_model().objects.first().blog_posts.first()
    
    """

    class Meta:
        abstract = True

    title = models.CharField(_('title'), max_length=350)
    content = RichTextUploadingField(_('content'))
    slug = models.SlugField(_('slug'), unique=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='%(class)s_posts',
                               verbose_name=_('author'))
    thumbnail = models.ImageField(_('thumbnail'),
                                  upload_to=f'thumbnails/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                  blank=True, null=True)
    thumbnail_alt = models.CharField(_('thumbnail alt'), max_length=350, blank=True)


@receiver(pre_save, sender=BasicPost)
def base_post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
