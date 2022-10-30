from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver

from blog.models import Category
from utils.general.models import Seo, Status, BasicPost, DateBasic
from utils.utile.unique_slug_generator import unique_slug_generator


class Post(Seo, DateBasic, BasicPost, Status):
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'), related_name='posts')

    def __str__(self):
        return self.title


