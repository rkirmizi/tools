from django.conf.urls.defaults import *
from django.conf import settings
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
	    {
	    	'document_root': settings.MEDIA_ROOT,
			'show_indexes': True
		}),

#    (r'^admin/', include(admin.site.urls)),
)
