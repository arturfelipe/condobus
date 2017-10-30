from django.db import models
from django.utils.translation import ugettext_lazy as _


class Bus(models.Model):
    name = models.CharField(_('Nome'), max_length=200)

    class Meta:
        verbose_name = _('Ônibus')

    def __str__(self):
        return self.name
