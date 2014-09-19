from django.conf.urls import patterns, include, url
from django.contrib import admin

from killedbycops.admin import admin_site

urlpatterns = patterns('',
    url(r'^$', 'killedbycops.views.home', name='home'),
    url(r'^admin/', include(admin_site.urls)),
)
