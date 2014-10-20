from tastypie import fields, utils
from tastypie.resources import ModelResource
from fatalencounters.models import FatalEncounter


class FatalEncounterResource(ModelResource):

    class Meta:
        queryset = FatalEncounter.objects.filter(proofed=True)
        list_allowed_methods = ['get', ]
        detail_allowed_methods = ['get', ]
        excludes = ['proofed', 'photo_url', 'source_url']
        resource_name = 'fatalencounters'

        filtering = {
            'date_of_injury': ['exact', 'lt', 'lte', 'gte', 'gt'],
            'state': ['exact', ],
            'city': ['exact', ],
            'race': ['exact', ],
        }