#-*- coding: utf-8 -*-

from articles.models import Category


def category(request):
    return {'cat': Category.objects.filter(show=True)}
