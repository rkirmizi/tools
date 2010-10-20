from django.conf.urls.defaults import *

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
#    (r'^admin/', include(admin.site.urls)),
)
