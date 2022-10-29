from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.general.models import DateBasic
from utils.general.models import Seo
from utils.general.models import Taxonomy
from utils.general.models import Status


class Category(Seo, Taxonomy, DateBasic, Status):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='categories',
                                        verbose_name=_('parent category'), blank=True, null=True)

    def __str__(self):
        return self.title
