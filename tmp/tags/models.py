# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.db import models


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
