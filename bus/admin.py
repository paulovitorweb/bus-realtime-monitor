from django.contrib.gis import admin
from bus.models import Terminal


class TerminalAdmin(admin.OSMGeoAdmin):
    pass

admin.site.register(Terminal, TerminalAdmin)
