from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver

from blog.models import Category
from utils.general.models import Seo, Status, BasicPost, DateBasic,LanguageStatus
from utils.utile.unique_slug_generator import unique_slug_generator


class Post(Seo, DateBasic, BasicPost, Status,LanguageStatus):
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'), related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


@receiver(pre_save, sender=Post)
def base_post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
