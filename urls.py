from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from paraphrase.views import show_section, show_actor
from paraphrase.sections import sections
urlpatterns = patterns('',
    # Examples:
    (r'^$', show_section),
    (r'^actors/(.*)$', show_actor),
    # url(r'^paraphrase/', include('paraphrase.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls')),       
)

for section in sections:
    urlpatterns += patterns('', ('^(' + section['id'] + ')$', show_section))

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
