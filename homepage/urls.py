from django.conf.urls import patterns, url, include
from django.conf import settings
from .views import about, product, contact, withyou, license, privacy, setlang, robots
from .views import ResumeAdd, ResumeDetail, ResumeUpdate, ResumeDelete, resume_inform

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', about, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^product/$', product, name='product'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^contact/withyou/$', withyou, name='withyou'),
    url(r'^license/$', license, name='license'),
    url(r'^privacy/$', privacy, name='privacy'),

    # for resume
    url(r'^resume/new/$', ResumeAdd.as_view(), name='resume_add'),
    url(r'^resume/(?P<slug>\w+)/$', ResumeDetail.as_view(), name='resume_detail'),
    url(r'^resume/(?P<slug>\w+)/update/$', ResumeUpdate.as_view(), name='resume_update'),
    url(r'^resume/(?P<slug>\w+)/delete/$', ResumeDelete.as_view(), name='resume_delete'),
    url(r'^resume/(?P<slug>\w+)/inform/$', resume_inform, name='resume_inform'),

    url(r'^lang/(?P<lang_code>.*)/$', setlang, name='setlang'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^robots.txt$', robots, name='robots'),

    url(r'^summernote/', include('django_summernote.urls')),
)

# for development
if settings.DEBUG:
    urlpatterns = urlpatterns + patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )

# for rosetta
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns(
        '',
        url(r'^rosetta/', include('rosetta.urls')),
    )
