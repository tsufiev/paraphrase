from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from paraphrase.views import show_section, show_gallery, show_photo
from paraphrase.sections import sections

from django.shortcuts import redirect
# from django.core.urlresolvers import reverse

urlpatterns = patterns('',
    url(r'^$', show_section),
    url(r'^actors/$', show_gallery),
    url(r'^actors/(?P<actor>[\-\d\w]+)/$', show_photo),
    url(r'^photos/$', show_gallery, {'slug': None, 'page': '1'}),
    url(r'^photos/page/(?P<page>\d+)/$', show_gallery, {'slug': None}),
    url(r'^photos/gallery/(?P<slug>[\-\d\w]+)/$', show_gallery, {'page': '1'}, name='gallery'),
    url(r'^photos/gallery/(?P<slug>[\-\d\w]+)/page/(?P<page>\d+)/$', show_gallery),
    url(r'^photos/gallery/(?P<gallery>[\-\d\w]+)/photo/(?P<photo>[\-\d\w]+)/$', show_photo, name='photo'),
    url(r'^admin/', include(admin.site.urls)),
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
