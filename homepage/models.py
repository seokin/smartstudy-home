# -*- coding: utf-8 -*-
from django.db import models
from library import uploaded_filepath


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
    picture = models.ImageField(verbose_name=u'사진', upload_to=uploaded_filepath)
    comment = models.TextField(verbose_name=u'한마디', blank=True)
    email = models.EmailField(verbose_name=u'이메일', null=True, blank=True)
    home = models.URLField(verbose_name=u'홈페이지', null=True, blank=True)
    facebook = models.URLField(verbose_name=u'페이스북', null=True, blank=True)
    twitter = models.CharField(verbose_name=u'트위터', null=True, blank=True, max_length=50)
    github = models.CharField(verbose_name=u'깃허브', null=True, blank=True, max_length=50)

    def firstname_eng(self):
        return self.name_eng.partition(' ')[0]

    def lastname_eng(self):
        return self.name_eng.partition(' ')[2]

    def __unicode__(self):
        return self.name


class App(models.Model):
    title = models.CharField(verbose_name=u'제목', max_length=100,
                             null=True, blank=True)
    title_eng = models.CharField(verbose_name=u'영문 제목', max_length=100,

                                 null=True, blank=True)
    subtitle = models.CharField(verbose_name=u'부제', max_length=100,
                                null=True, blank=True)
    subtitle_eng = models.CharField(verbose_name=u'영문 부제', max_length=100,
                                    null=True, blank=True)

    cms_id = models.CharField(verbose_name=u'앱 아이디', max_length=255)
    icon = models.ImageField(upload_to=uploaded_filepath)
    appid_ios = models.CharField(max_length=255, null=True, blank=True)
    appid_googleplay = models.CharField(max_length=255, null=True, blank=True)

    desc = models.TextField(verbose_name=u'짧은 소개', blank=True)
    desc_more = models.TextField(verbose_name=u'추가로 긴 소개', blank=True)
    desc_eng = models.TextField(verbose_name=u'짧은 영문 소개', blank=True)
    desc_more_eng = models.TextField(verbose_name=u'추가로 긴 영문 소개', blank=True)

    launched = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return '%s(%s)' % (self.title, self.cms_id)


class AppImage(models.Model):
    app = models.ForeignKey(App, related_name='images')
    image = models.ImageField(upload_to=uploaded_filepath)


class AppCategory(models.Model):
    uid = models.CharField(max_length=255)
    title = models.CharField(verbose_name=u'카테고리 명', max_length=255, null=True, blank=True)
    title_eng = models.CharField(verbose_name=u'카테고리 영문명', max_length=255, null=True, blank=True)
    app = models.ManyToManyField(App, blank=True)
