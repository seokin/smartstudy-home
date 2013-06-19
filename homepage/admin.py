# -*- coding: utf-8 -*-
from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from easymode.i18n.admin.decorators import L10n
from models import Crew, App, AppImage, AppCategory


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


class AppAdmin(MarkdownModelAdmin):
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
