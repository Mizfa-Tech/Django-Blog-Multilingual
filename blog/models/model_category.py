from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from utils.general.models import DateBasic
from utils.general.models import Seo
from utils.general.models import Taxonomy
from utils.general.models import Status
from utils.general.models import LanguageStatus
from utils.utile.unique_slug_generator import unique_slug_generator


class Category(Seo, Taxonomy, DateBasic, Status, LanguageStatus):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='categories',
                                        verbose_name=_('parent category'), blank=True, null=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Category)
def base_post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
