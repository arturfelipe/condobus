from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TransportConfig(AppConfig):
    name = 'transport'
    verbose_name = _('Transport')
