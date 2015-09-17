# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.template import RequestContext
from django.shortcuts import render
from articles.models import Article
from tags.models import Tags


def tag(request, slug_title):
    tag = Tags.objects.get(slug_title=slug_title)
    art_with_tag = []
    for n in Article.objects.filter(show=True):
        if n.tags.filter(slug_title=slug_title).count():
            art_with_tag.append(n)
    return render(request,
        'tag.html',
        {
            'tag': tag,
            'art_with_tag': art_with_tag,
        },
    )
