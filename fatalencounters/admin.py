from django.contrib import admin
from fatalencounters.models import FatalEncounter, County

class FatalEncounterAdmin(admin.ModelAdmin):
  list_filter = ('gender', 'race', 'proofed')
  list_display = ('name', 'age', 'city', 'county', 'state', 'race', 'date_of_injury', 'photo_tag')
  search_fields = ('name','city','county','state')
  date_hierarchy = 'date_of_injury'
  fieldsets = [
    ('Biographical', {'fields': ['name','age','gender','race']}),
    ('Incident', {'fields': ['date_of_injury','city','county','state','agency_responsible']}),
    ('Sources', {'fields': ['source_url','photo_url']}),
  ]

class CountyAdmin(admin.ModelAdmin):
  list_display = ('fips_code', 'name', 'state')
  list_filter = ('state',)
  search_fields = ('name',)


admin.site.register(FatalEncounter, FatalEncounterAdmin)
admin.site.register(County, CountyAdmin)