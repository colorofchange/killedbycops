from django.contrib import admin
from models import County, StoryEmbed


class CountyAdmin(admin.ModelAdmin):
    list_display = ('fips_code', 'name', 'state')
    list_filter = ('state',)
    search_fields = ('name', )

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(CountyAdmin, self).get_search_results(request, queryset, search_term)
        if search_term.isdigit():
            state_ansi = None
            county_ansi = None

            if len(search_term) == 2:
                state_ansi = search_term
            elif len(search_term) == 3:
                county_ansi = search_term
            elif len(search_term) == 5:
                state_ansi = search_term[:2]
                county_ansi = search_term[2:]
            else:
                return queryset, use_distinct

            qs = self.model.objects.all()
            if state_ansi:
                qs = qs.filter(state_ansi=state_ansi)
            if county_ansi:
                qs = qs.filter(county_ansi=county_ansi)
            queryset = qs
        return queryset, use_distinct


class StoryEmbedAdmin(admin.ModelAdmin):
    list_display = ('name', 'county', 'url', 'image_tag')
    raw_id_fields = ('county', )

admin.site.register(County, CountyAdmin)
admin.site.register(StoryEmbed, StoryEmbedAdmin)
