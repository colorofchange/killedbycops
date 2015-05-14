from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from tastypie.api import Api
from fatalencounters.api import FatalEncounterResource

v1_api = Api(api_name='v1')
v1_api.register(FatalEncounterResource())

urlpatterns = patterns('',
    url(r'^$', 'map.views.map', name='map'),
    url(r'^map/stories\.json$', 'map.views.stories_json', name='stories_json'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.autodiscover()
