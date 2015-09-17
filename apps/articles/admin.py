# -*- coding: utf-8 -*-

from django.contrib import admin
from articles.models import Article, Category, Author, Comment, Tags


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate')
    list_filter = ('pubdate',)
    search_fields = ('title', 'preview')
    filter_horizontal = ('tags', 'comment')

    prepopulated_fields = {'slug_title': ('title',)}

    class Media:
        js = [
            '/media/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/media/grappelli/tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'preview', 'content')

    class Media:
        js = [
            '/media/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/media/grappelli/tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(Category, CategoryAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(Author, AuthorAdmin)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    prepopulated_fields = {'slug_title': ('title', )}

admin.site.register(Tags, TagsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'show')
    search_fields = ('title', 'email')
    list_filter = ('date', 'show', 'article')

admin.site.register(Comment, CommentAdmin)
