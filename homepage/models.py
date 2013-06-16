# -*- coding: utf-8 -*-
from django.db import models
from easymode.i18n.decorators import I18n
from easy_thumbnails.fields import ThumbnailerImageField as ImageField
from library import uploaded_filepath


@I18n('name', 'title', 'nick', 'comment', )
class Crew(models.Model):
    class Meta:
        ordering = ['name_ko']

    nick = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    uid = models.CharField(max_length=50, null=True, blank=True)
    picture = ImageField(upload_to='crew/iconic/')
    picture_big = ImageField(upload_to='crew/big/')
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


@I18n('title', 'subtitle', 'desc', 'desc_more', 'appid_appstore', 'appid_playstore', )
class App(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    icon = ImageField(upload_to=uploaded_filepath)
    appid_appstore = models.CharField(max_length=255, null=True, blank=True)
    appid_playstore = models.CharField(max_length=255, null=True, blank=True)

    desc = models.TextField(blank=True)
    desc_more = models.TextField(blank=True)

    launched = models.DateField(auto_now_add=True)

    def link_appstore(self):
        return "https://itunes.apple.com/app/id%s" % self.appid_appstore

    def link_playstore(self):
        return "https://play.google.com/store/apps/details?id=%s" % self.appid_playstore

    def has_landscape_images(self):
        return self.images.all()[0].image.width > self.images.all()[0].image.height

    def __unicode__(self):
        return self.title


class AppImage(models.Model):
    app = models.ForeignKey(App, related_name='images')
    image = ImageField(upload_to=uploaded_filepath)


@I18n('title', )
class AppCategory(models.Model):
    uid = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    app = models.ManyToManyField(App, blank=True)
