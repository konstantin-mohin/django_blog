# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render
from django.db.models import Count
from django.db.models import Q

from simple_pages.models import Simpl
from articles.models import Article, Comment


def main_page(request):
    art = Article.objects.select_related().order_by('-pubdate')
    return render(
        request,
        'base.html',
        {
            'smpl': Simpl.objects.get(pk=1),
            'articles': art,
            'commented': art.annotate(ct=Count('comment')).filter(ct__gt=0),
            'author': Comment.objects.filter(
                Q(title__startswith='dalai') &
                Q(title__endswith='lama')).count(),
            'month': art.filter(show=True, pubdate__month=2).count(),
        },
    )
