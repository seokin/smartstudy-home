# -*- coding: utf-8 -*-
from django.db import models
from easymode.i18n.decorators import I18n
from library import uploaded_filepath


@I18n('name', 'title', 'nick', 'comment', )
class Crew(models.Model):
    class Meta:
        ordering = ['name_ko']

    nick = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    uid = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(upload_to='crew/iconic/')
    picture_big = models.ImageField(upload_to='crew/big/')
    comment = models.TextField(blank=True)
    email = models.EmailField(null=True, blank=True)
    home = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.CharField(null=True, blank=True, max_length=50)
    github = models.CharField(null=True, blank=True, max_length=50)

    def firstname(self):
        return self.name.partition(' ')[0]

    def lastname(self):
        return self.name.partition(' ')[2]

    def __unicode__(self):
        return self.name


@I18n('title', 'subtitle', 'desc', 'desc_more', )
class App(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    cms_id = models.CharField(max_length=255)
    icon = models.ImageField(upload_to=uploaded_filepath)
    appid_appstore = models.CharField(max_length=255, null=True, blank=True)
    appid_playstore = models.CharField(max_length=255, null=True, blank=True)

    desc = models.TextField(blank=True)
    desc_more = models.TextField(blank=True)

    launched = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return '%s(%s)' % (self.title, self.cms_id)


class AppImage(models.Model):
    app = models.ForeignKey(App, related_name='images')
    image = models.ImageField(upload_to=uploaded_filepath)


@I18n('title', )
class AppCategory(models.Model):
    uid = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    app = models.ManyToManyField(App, blank=True)
