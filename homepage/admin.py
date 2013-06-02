# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Crew


class CrewAdmin(admin.ModelAdmin):
    def picture(self):
        return '<a href="%s"><img src="%s" width="50" /></a>' % (self.id, self.picture.url)

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
