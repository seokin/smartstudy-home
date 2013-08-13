# -*- coding: utf-8 -*-
from django.db import models
from easymode.i18n.decorators import I18n
from easy_thumbnails.fields import ThumbnailerImageField as ImageField
from django.forms import CharField
from django_summernote.widgets import SummernoteWidget
from jsonfield import JSONField
from library import uploaded_filepath
from uuid import uuid4


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


class Job(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    active = models.BooleanField(default=True)

    begin = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Resume(models.Model):
    apply_to = models.ForeignKey(Job)
    hash_code = models.CharField(max_length=255, editable=False, db_index=True)

    email = models.EmailField(max_length=255, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    desc = JSONField()
    attachment = models.FileField(upload_to=uploaded_filepath, null=True, blank=True)

    applied = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @classmethod
    def _jsonfields(cls):
        from collections import OrderedDict
        return OrderedDict([
            ('linkedin', {'field': CharField(max_length=255)}),
            ('homepage', {'field': CharField(max_length=255)}),
            ('github', {'field': CharField(max_length=255)}),
            ('selfdesc', {'field': CharField(widget=SummernoteWidget())}),
            ('resume', {'field': CharField(widget=SummernoteWidget())}),
        ])

    def _generate_key(self):
        return (str(uuid4())).replace('-', '')

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.hash_code = self._generate_key()
        super(Resume, self).save()

    def __unicode__(self):
        return '%s(%s)' % (self.name, self.email)
