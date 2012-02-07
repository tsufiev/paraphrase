from django.conf.urls.defaults import patterns, include, url
import paraphrase.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', paraphrase.views.home),
    url(r'^actors$', paraphrase.views.actors),
    # Examples:
    # url(r'^$', 'paraphrase.views.home', name='home'),
    # url(r'^paraphrase/', include('paraphrase.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls')),       
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
