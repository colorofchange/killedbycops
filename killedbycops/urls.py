from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'killedbycops.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
admin.autodiscover()