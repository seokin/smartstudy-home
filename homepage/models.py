# -*- coding: utf-8 -*-
from django.db import models


class Crew(models.Model):
    class Meta:
        ordering = ['name_eng']

    nick = models.CharField(verbose_name=u'별명', max_length=50)
    title = models.CharField(verbose_name=u'역할', max_length=50)
    name = models.CharField(verbose_name=u'이름', max_length=50,
                            null=True, blank=True)
    name_eng = models.CharField(verbose_name=u'영문 이름', max_length=100,
                                null=True, blank=True)
    uid = models.CharField(verbose_name=u'아이디', max_length=50,
                           null=True, blank=True)
    picture = models.ImageField(verbose_name=u'사진', upload_to='crew')
    comment = models.TextField(verbose_name=u'한마디', blank=True)
    email = models.EmailField(verbose_name=u'이메일', null=True, blank=True)
    home = models.URLField(verbose_name=u'홈페이지', null=True, blank=True)
    facebook = models.URLField(verbose_name=u'페이스북', null=True, blank=True)
    twitter = models.CharField(verbose_name=u'트위터', null=True, blank=True, max_length=50)


class App(models.Model):
    name = models.CharField(verbose_name=u'이름', max_length=50,
                            null=True, blank=True)
    name_eng = models.CharField(verbose_name=u'영문 이름', max_length=100,
                                null=True, blank=True)
    uid = models.CharField(verbose_name=u'앱 아이디', max_length=255,
                           null=True, blank=True)
    appid_ios = models.ImageField(verbose_name=u'사진', upload_to='crew')
    appid_android = models.ImageField(verbose_name=u'사진', upload_to='crew')
    twitter = models.CharField(verbose_name=u'트위터', null=True, blank=True, max_length=50)
