from django.contrib import admin
from fatalencounters.models import FatalEncounter, County

from admin_exporter.actions import export_as_csv_action


class FatalEncounterAdmin(admin.ModelAdmin):
    list_filter = ('gender', 'race', 'state', 'proofed')
    list_display = ('name', 'age', 'city', 'county', 'state', 'race', 'date_of_injury', 'photo_tag')
    search_fields = ('name', 'city', 'county', 'state')
    date_hierarchy = 'date_of_injury'
    fieldsets = [
        ('Biographical', {'fields': ['name', 'age', 'gender', 'race']}),
        ('Incident', {'fields': ['date_of_injury', 'city', 'county', 'state', 'agency_responsible']}),
        ('Sources', {'fields': ['source_url', 'photo_url']}),
    ]


class CountyAdmin(admin.ModelAdmin):
    list_display = ('fips_code', 'name', 'state')
    list_filter = ('state',)
    search_fields = ('name',)

admin.site.add_action(export_as_csv_action)
admin.site.register(FatalEncounter, FatalEncounterAdmin)
admin.site.register(County, CountyAdmin)
