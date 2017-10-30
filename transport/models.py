from django.db import models
from django.utils.translation import ugettext_lazy as _


class Bus(models.Model):
    name = models.CharField(_('Name'), max_length=200)

    class Meta:
        verbose_name = _('Bus')
        verbose_name_plural = _('Buses')

    def __str__(self):
        return self.name
