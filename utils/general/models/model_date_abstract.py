from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels


class DateBasic(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    created_at_jalali = jmodels.jDateTimeField(_('created at jalali'), auto_now_add=True)
    updated_at_jalali = jmodels.jDateTimeField(_('updated at jalali'), auto_now=True)
