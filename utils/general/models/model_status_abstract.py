from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    class Meta:
        abstract = True

    class Choices(models.TextChoices):
        PUBLISH = 'PU', _('Publish')
        INRIVIEW = 'IN', _('Inriview')
        PENDING = 'PE', _('Pending')

    status = models.CharField(_('status'),
                              max_length=2,
                              choices=Choices.choices,
                              default=Choices.PENDING,
                              )
