# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import mark_safe
from django.db.models import Q
from easymode.i18n.admin.decorators import L10n
from models import Crew, App, AppImage, AppCategory, Job, Resume, ResumeReview, Testimonial, Poster


@L10n(Crew)
class CrewAdmin(admin.ModelAdmin):
    def picture(self):
        return '<a href="%s"><img src="%s" width="24" /></a>' % (self.id, self.picture.url)

    picture.short_description = u'사진'
    picture.allow_tags = True

    class Media:
        css = {
            "all": ("css/admin.css",)
        }

    list_editable = ('title', 'name', 'email', 'nick', 'github', 'twitter', 'facebook', 'home',)
    list_display = ('id', picture, ) + ('title', 'name', 'email', 'nick', 'github', 'twitter', 'facebook', 'home',)
    list_display_links = ('id',)
    search_fields = ['title', 'uid', 'nick', 'comment', ]
    ordering = ('-id',)

admin.site.register(Crew, CrewAdmin)


class AppImageInline(admin.TabularInline):
    model = AppImage
    extra = 5


class AppAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title_ko', 'title_en',)
    inlines = [AppImageInline, ]
    search_fields = ['title_ko', 'title_en', ]
    ordering = ('-id',)

admin.site.register(App, AppAdmin)


@L10n(AppCategory)
class AppCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'title')
    list_editable = ('title',)
    search_fields = ['uid', 'title', ]
    ordering = ('-id',)

admin.site.register(AppCategory, AppCategoryAdmin)


class TestimonialAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'title', 'created',)
    search_fields = ['name', 'title', ]
    ordering = ('-id',)

admin.site.register(Testimonial, TestimonialAdmin)


def make_candidate(modeladmin, request, queryset):
    queryset.update(status='C')
make_candidate.short_description = _("Mark selected resume as candidate")


def make_archive(modeladmin, request, queryset):
    queryset.update(status='A')
make_archive.short_description = _("Archive selected resumes")


class ResumeAdmin(SummernoteModelAdmin):
    def link(self, obj):
        return mark_safe('<a href="%s">%s</a>' % (
            reverse('resume_detail', args=(obj.uuid,)),
            _('Link to resume')))

    def queryset(self, request):
        qs = super(ResumeAdmin, self).queryset(request)
        if request.GET.get('status__exact') == 'A':
            return qs
        return qs.filter(~Q(status='A'))

    link.allow_tags = True
    list_display = ('id', 'link', 'status', 'name', 'email', 'contact', 'apply_to', 'uuid', 'applied')
    list_filter = ('apply_to', 'status')
    search_fields = ['email', 'uuid', 'apply_to__name', 'name', 'desc']
    ordering = ('-id',)

    actions = [make_candidate, make_archive]

admin.site.register(Resume, ResumeAdmin)


class ResumeReviewAdmin(SummernoteModelAdmin):
    raw_id_fields = ('resume', )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        elif db_field.name == 'resume':
            kwargs['initial'] = request.GET.get('resume')
            return db_field.formfield(**kwargs)
        return super(ResumeReviewAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

admin.site.register(ResumeReview, ResumeReviewAdmin)

admin.site.register(Job, SummernoteModelAdmin)
admin.site.register(Poster, SummernoteModelAdmin)
