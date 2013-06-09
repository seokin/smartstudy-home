# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Crew, App, AppImage, AppCategory


class CrewAdmin(admin.ModelAdmin):
    def picture(self):
        return '<a href="%s"><img src="%s" width="24" /></a>' % (self.id, self.picture.url)

    picture.short_description = u'사진'
    picture.allow_tags = True

    class Media:
        css = {
            "all": ("css/admin.css",)
        }

    list_display = ('id', picture, 'title', 'name', 'name_eng', 'nick', 'email', 'github', 'twitter', 'facebook', 'home',)
    list_editable = ('title', 'name', 'name_eng', 'email', 'github', 'twitter', 'facebook', 'home',)
    list_display_links = ('id',)
    search_fields = ['title', 'uid', 'nick', 'comment', ]
    ordering = ('-id',)


admin.site.register(Crew, CrewAdmin)


class AppImageInline(admin.TabularInline):
    model = AppImage
    extra = 3


class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'title_eng', 'cms_id', 'launched', 'appid_appstore', 'appid_playstore',)
    list_editable = ('title', 'title_eng', 'appid_appstore', 'appid_playstore',)
    inlines = [AppImageInline, ]
    search_fields = ['title', 'title_eng', 'cms_id', ]
    ordering = ('-id',)


admin.site.register(App, AppAdmin)


class AppCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'title', 'title_eng')
    list_editable = ('title', 'title_eng',)
    search_fields = ['uid', 'title', 'title_eng', ]
    ordering = ('-id',)


admin.site.register(AppCategory, AppCategoryAdmin)
