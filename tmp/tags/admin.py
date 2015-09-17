# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.contrib import admin
from tags.models import Tags


class TagsAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )

    prepopulated_fields = {'slug_title': ('title', )}

    class Media:
        js = [
            '/media/js/admin_list_reorder.js',
        ]

admin.site.register(Tags, TagsAdmin)
