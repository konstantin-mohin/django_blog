#-*- coding: utf-8 -*-

from simple_pages.models import Simpl


def base(request):
    return {'smpl': Simpl.objects.order_by('-id').all()[0:1].get()}
