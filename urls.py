from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from paraphrase.views import show_section, show_gallery, show_photo, show_feedbacks, show_article
from sections.views import sections

from django.shortcuts import redirect

urlpatterns = patterns(
    '',
    url(r'^$', show_section),
    url(r'^articles/(?P<slug>[\-\d\w]+)/$', show_article),
    url(r'^actors/(?P<photo>[\-\d\w]+)/$', show_photo, name='actor'),
    url(r'^photos/gallery/(?P<gallery>[\-\d\w]+)/$', show_gallery, {'page': '1'}),
    url(r'^photos/gallery/(?P<gallery>[\-\d\w]+)/page/(?P<page>\d+)/$', show_gallery),
    url(r'^photos/gallery/(?P<gallery>[\-\d\w]+)/photo/(?P<photo>[\-\d\w]+)/$', show_photo, name='photo'),
    url(r'^feedbacks/$', show_feedbacks),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls')),
    )

for section in sections:
    urlpatterns += patterns(
        '', 
        ('^(' + section['id'] + ')/$', show_section, {'page': '1'}),
        ('^(' + section['id'] + ')/page/(?P<page>\d+)/$', show_section)
        )

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
