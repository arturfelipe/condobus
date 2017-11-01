from django.db import models
from django.utils.translation import ugettext_lazy as _


class Bus(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    organization = models.ForeignKey(
        'org.Organization',
        on_delete=models.CASCADE,
        related_name='buses',
        verbose_name=_('Organization')
    )

    class Meta:
        verbose_name = _('Bus')
        verbose_name_plural = _('Buses')

    def __str__(self):
        return self.name
