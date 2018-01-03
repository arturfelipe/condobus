from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from django.contrib.gis import admin
from transport.models import Bus, Route, StopPoint


class StopPointInline(admin.OSMGeoAdmin, admin.StackedInline):
    model = StopPoint
    can_delete = False
    verbose_name_plural = 'StopPoints'

    def __init__(self, parent_model, admin_site):
        self.admin_site = admin_site
        self.parent_model = parent_model
        self.opts = self.model._meta
        self.has_registered_model = admin_site.is_registered(self.model)
        overrides = FORMFIELD_FOR_DBFIELD_DEFAULTS.copy()
        overrides.update(self.formfield_overrides)
        self.formfield_overrides = overrides
        if self.verbose_name is None:
            self.verbose_name = self.model._meta.verbose_name
        if self.verbose_name_plural is None:
            self.verbose_name_plural = self.model._meta.verbose_name_plural


class RouteAdmin(admin.ModelAdmin):
    inlines = [StopPointInline,]


admin.site.register(Bus)
admin.site.register(Route, RouteAdmin)
