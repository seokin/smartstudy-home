# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Avg
from easymode.i18n.decorators import I18n
from easy_thumbnails.fields import ThumbnailerImageField as ImageField
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
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


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    tldr = models.TextField()
    desc = models.TextField()
    picture = ImageField(upload_to='testimonial/')
    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Resume(models.Model):
    DRAFT = 'D'
    SUBMIT = 'S'
    ARCHIVE = 'A'
    CANDIDATE = 'C'
    STATUS = (
        (DRAFT, _('Draft')),
        (SUBMIT, _('Submitted')),
        (CANDIDATE, _('Candidate')),
        (ARCHIVE, _('Archived')),
    )

    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT, editable=False)
    apply_to = models.ForeignKey(Job, verbose_name=_('Apply to'))
    uuid = models.CharField(max_length=255, editable=False, db_index=True)

    email = models.EmailField(max_length=255, db_index=True, verbose_name=_('Email'))
    name = models.CharField(max_length=100, db_index=True, verbose_name=_('Full name'))
    contact = models.CharField(max_length=100, verbose_name=_('Contact / Phone'))
    desc = JSONField()
    attachment = models.FileField(upload_to=uploaded_filepath, null=True, blank=True, verbose_name=_('Resume as file (optional)'))

    applied = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @classmethod
    def descfields(cls):
        from collections import OrderedDict
        return OrderedDict([
            ('linkedin', {'field': forms.CharField(max_length=255, required=False, label=_('LinkedIn URL (optional)'))}),
            ('homepage', {'field': forms.URLField(max_length=255, required=False, label=_('Homepage URL (optional)'))}),
            ('github', {'field': forms.CharField(max_length=255, required=False, label=_('Github id (optional)'))}),
            ('description', {'field': forms.CharField(widget=SummernoteWidget(), required=False, label=_('Self description'))}),
            ('resume', {'field': forms.CharField(widget=SummernoteWidget(), required=False, label=_('Education / Experience'))}),
        ])

    def _generate_key(self):
        return (str(uuid4())).replace('-', '')

    def get_absolute_url(self):
        return reverse('resume_detail', args=(self.uuid,))

    def in_draft(self):
        return self.status == Resume.DRAFT

    def avg_rating(self):
        rating = ResumeReview.objects.filter(resume=self).aggregate(avg_rating=Avg('rating'))['avg_rating']
        if not rating:
            rating = ''
        return rating

    def rated_by(self):
        return ResumeReview.objects.filter(resume=self).values_list('user__id', flat=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.uuid = self._generate_key()
        super(Resume, self).save()

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)


class ResumeReview(models.Model):
    resume = models.ForeignKey(Resume)
    user = models.ForeignKey(User)
    rating = models.IntegerField()
    desc = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s (by %s)' % (self.resume, self.user)


class Poster(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    picture = ImageField(upload_to='poster/')
    active = models.BooleanField(default=True)
    desc = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('poster', args=(self.uuid,))

    def __unicode__(self):
        return self.title
