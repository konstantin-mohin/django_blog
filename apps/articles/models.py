# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime


class Author(models.Model):
    title = models.CharField('Имя автора', max_length=256)

    class Meta:
        ordering = ('title', )
        verbose_name = 'Автора'
        verbose_name_plural = 'Авторы'

    def __unicode__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    slug_title = models.SlugField('Ссылка', max_length=128, unique=True)
    position = models.IntegerField('Позиция', blank=True, null=True)

    def save(self, *args, **kwargs):
        model = self.__class__
        if self.position is None:
            try:
                last = model.objects.order_by('-position')[0]
                self.position = last.position + 1
            except:
                self.position = 0
        return super(Tags, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('position', )
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=500)
    slug_title = models.SlugField('Имя для ссылки', unique=True)
    preview = models.CharField('Анонс', max_length=1550)
    pubdate = models.DateTimeField('Дата публикации', auto_now_add=True)
    content = models.TextField('Содержание')
    category = models.ForeignKey('Category', verbose_name='Категория')
    show = models.BooleanField('Показывать', default=True)
    author = models.ForeignKey(Author, verbose_name='Автор статьи', blank=True)
    tags = models.ManyToManyField(
        'Tags', verbose_name=u'Теги',
        related_name='tag', blank=True
    )
    comment = models.ManyToManyField(
        'Comment', verbose_name=u'Коментарий',
        related_name='comments', blank=True, null=True
    )

    def save(self):
        if not self.id:
            self.slug_title = slugify(self.slug_title)
        super(Article, self).save()

    class Meta:
        ordering = ('-pubdate', )
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

    def __unicode__(self):
        return self.title


class Category(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    slug_title = models.SlugField('Имя для ссылки', unique=True)
    preview = models.CharField('Анонс', max_length=1000, blank=True, null=True)
    content = models.TextField('Содержание', blank=True, null=True)
    position = models.IntegerField('Позиция', blank=True, null=True)
    show = models.BooleanField('Показывать', default=True)

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.id:
            self.slug_title = slugify(self.slug_title)
        super(Category, self).save()

    class Meta:
        ordering = ('position', )
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Comment(models.Model):
    article = models.ForeignKey(
        Article, verbose_name='К статье', related_name='article'
    )
    user = models.ForeignKey(User, verbose_name='Пользователь', blank=True)
    title = models.CharField('Имя', max_length=128, blank=True, null=True)
    email = models.EmailField('E-mail', max_length=100, blank=True, null=True)
    site = models.CharField('Сайт', max_length=128, blank=True, null=True)
    content = models.TextField('Комментарий', max_length=5000, blank=True)
    date = models.DateTimeField('Дата и время', default=datetime.now())
    show = models.BooleanField('Показывать', default=True)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = 'Комментарий к статьи'
        verbose_name_plural = 'Комментарии к статьям'
