#-*- coding: utf-8 -*-

from django.conf.urls.defaults import *


urlpatterns = patterns(
    'articles.views',
    url(r'tag/(.*)/$', 'tag', name='tag'),
    url(r'comment/(.*)/$', 'comment', name='com'),
    url(r'(.*)/(.*)/$', 'art_inside', name='art_inside'),
    url(r'(.*)/$', 'category_inside', name='category_inside'),
)
