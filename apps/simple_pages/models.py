# -*- coding: utf-8 -*-

from django.db import models


class Simpl(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    logo = models.ImageField('Логотип', upload_to='img', blank=True, null=True)
    main_banner = models.CharField(
        'Текст под логотипом', max_length=252, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=128)
    emil = models.CharField('E-mail', max_length=128)
    skype = models.CharField('Skype', max_length=128)
    metakey = models.CharField(
        'Meta key', max_length=255, blank=True, null=True)
    metades = models.CharField(
        'Meta des', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Главную страницу"
        verbose_name_plural = "Главная"
