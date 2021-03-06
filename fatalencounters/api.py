from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import ReadOnlyAuthorization
from tastypie.cache import SimpleCache

from fatalencounters.models import FatalEncounter
from fatalencounters.serializers import PrettyJSONSerializer


class FatalEncounterResource(ModelResource):
    race = fields.CharField(attribute="get_race_display")
    county_fips = fields.CharField(attribute='county_fips', readonly=True)

    class Meta:
        queryset = FatalEncounter.objects.filter(proofed=True)
        list_allowed_methods = ['get', ]
        detail_allowed_methods = ['get', ]
        authorization = ReadOnlyAuthorization()

        excludes = ['proofed', 'photo_url', 'source_url']
        resource_name = 'fatalencounters'
        max_limit = 10000

        filtering = {
            'date_of_injury': ['exact', 'lt', 'lte', 'gte', 'gt'],
            'state': ['exact', ],
            'city': ['exact', ],
            'race': ['exact', ],
        }

        cache = SimpleCache(timeout=10)
        serializer = PrettyJSONSerializer()
