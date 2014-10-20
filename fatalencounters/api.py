from tastypie.resources import ModelResource
from fatalencounters.models import FatalEncounter


class FatalEncounterResource(ModelResource):

    class Meta:
        queryset = FatalEncounter.objects.all()
        list_allowed_methods = ['get', ]
        detail_allowed_methods = ['get']
        resource_name = 'fatalencounters'