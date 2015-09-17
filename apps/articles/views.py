# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render
from django.utils import simplejson

from articles.models import Article, Category, Comment, Tags
from articles.forms import FormCommentNonAuth, FormCommentAuth


def art_inside(request, slug_title, slug):
    slug = slug
    art = Article.objects.select_related(
        'tags').get(slug_title=slug, show=True)
    return render(
        request,
        'article.html',
        {
            'art': art,
        },
    )


def category_inside(request, slug_title):
    category = Category.objects.filter(
        slug_title__contains=slug_title, show=True
    )
    return render(
        request,
        'category.html',
        {
            'category': category,
            'articl': Article.objects.filter(show=True, category__in=category),
        },
    )


def tag(request, slug_title):
    tag = Tags.objects.get(slug_title=slug_title)
    art_with_tag = []
    for n in Article.objects.filter(show=True):
        if n.tags.filter(slug_title=slug_title).count():
            art_with_tag.append(n)
    return render(
        request,
        'tag.html',
        {
            'tag': tag,
            'art_with_tag': art_with_tag,
        },
    )


def comment(request, id):
    if request.method == 'POST' and request.is_ajax():
        art = Article.objects.get(id=id)
        if request.user.is_authenticated():
            form = FormCommentAuth(data=request.POST)
            user = request.user
        else:
            form = FormCommentNonAuth(data=request.POST)
            user = None
        rdict = {'valid': 'true'}
        if form.is_valid():
            cd = form.cleaned_data
            if user:
                comment = Comment(
                    title=art.author, email=user.email,
                    content=cd['comment'], article=art
                )
                comment.save()
                art.comment.add(comment)
                json = simplejson.dumps(rdict, ensure_ascii=False)
                return HttpResponse(json, mimetype='text/javascript')
            else:
                comment = Comment(
                    title=cd['comname'], email=cd['comemail'],
                    content=cd['comment'], article=art, site=cd['comsite']
                )
                comment.save()
                art.comment.add(comment)
                json = simplejson.dumps(rdict, ensure_ascii=False)
                return HttpResponse(json, mimetype='text/javascript')
        else:
            rdict.update({'valid': 'false'})
            d = {}
            for e in form.errors.iteritems():
                d.update({e[0]: unicode(e[1].as_text())})
                rdict.update({'errs': d})
        json = simplejson.dumps(rdict, ensure_ascii=False)
        return HttpResponse(json, mimetype='text/javascript')
