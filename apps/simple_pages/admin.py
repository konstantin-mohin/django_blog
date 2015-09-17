# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.contrib import admin
from simple_pages.models import Simpl


class SimplAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_banner', )
    search_fields = ('title', 'main_banner',)

admin.site.register(Simpl, SimplAdmin)
