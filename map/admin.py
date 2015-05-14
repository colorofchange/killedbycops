from django.contrib import admin
from models import County, StoryEmbed


class CountyAdmin(admin.ModelAdmin):
    list_display = ('fips_code', 'name', 'state')
    list_filter = ('state',)
    search_fields = ('name',)


class StoryEmbedAdmin(admin.ModelAdmin):
    raw_id_field = ('county', )

admin.site.register(County, CountyAdmin)
admin.site.register(StoryEmbed, StoryEmbedAdmin)
