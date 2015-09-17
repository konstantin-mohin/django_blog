# -*- coding: utf-8 -*-
""" main urls """

from django.conf.urls.defaults import patterns, include
from blog_task.settings import MEDIA_ROOT, STATIC_ROOT
from django.contrib import admin
from simple_pages.views import main_page
admin.autodiscover()


urlpatterns = patterns(
    '',
    (r'^media/(.*)$', 'django.views.static.serve',
     {'document_root': MEDIA_ROOT, 'show_indexes': True}),
    (r'^static/(.*)$', 'django.views.static.serve',
     {'document_root': STATIC_ROOT, 'show_indexes': True}),
    (r'^$', main_page),
    (r'^articles/', include('articles.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'', include('django.contrib.flatpages.urls')),
)
