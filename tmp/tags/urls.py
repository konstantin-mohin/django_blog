#-*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('tags.views',
    url(r'(.*)/$', 'tag', name = 'tag'),
)