from django.contrib import admin
from fatalencounters.models import FatalEncounter

class FatalEncounterAdmin(admin.ModelAdmin):
  list_filter = ('gender', 'race', 'proofed')
  list_display = ('name', 'age', 'gender', 'race', 'date_of_injury', 'photo_tag')
  search_fields = ('name','city','state')
  date_hierarchy = 'date_of_injury'
  fieldsets = [
    ('Biographical', {'fields': ['name','age','gender','race']}),
    ('Incident', {'fields': ['date_of_injury','city','state','agency_responsible']}),
    ('Sources', {'fields': ['source_url','photo_url','uid']}),
  ]

admin.site.register(FatalEncounter, FatalEncounterAdmin)
