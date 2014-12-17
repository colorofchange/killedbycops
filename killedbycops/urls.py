from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api
from fatalencounters.api import FatalEncounterResource

v1_api = Api(api_name='v1')
v1_api.register(FatalEncounterResource())

urlpatterns = patterns('',
    #url(r'^$', 'killedbycops.views.home', name='home'),
    url(r'^$', 'map.views.map', name='map'),
    url(r'^map-test/', 'killedbycops.views.redirect_home', name='redirect_home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
admin.autodiscover()