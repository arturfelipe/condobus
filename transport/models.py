from django.db import models
from django.utils.translation import ugettext_lazy as _
from org.models import Organization


class Bus(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='buses',
        verbose_name=_('Organization')
    )

    class Meta:
        verbose_name = _('Bus')
        verbose_name_plural = _('Buses')

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='routes',
        verbose_name=_('Organization')
    )

    class Meta:
        verbose_name = _('Route')
        verbose_name_plural = _('Routes')

    def __str__(self):
        return self.name
