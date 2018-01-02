from django.contrib.gis import admin
from transport.models import Bus, Route, StopPoint

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(StopPoint, admin.OSMGeoAdmin)
