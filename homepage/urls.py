from django.conf.urls import patterns, url, include
from django.conf import settings
from .views import about, product, contact, withyou, license, privacy, setlang, robots
from .views import ResumeAdd, ResumeList, ResumeDetail, ResumeUpdate, ResumeDelete, resume_inform
from .views import ResumeReviewAdd, ResumeReviewUpdate, ResumeReviewDelete
from .views import TestimonialDetail
from .views import PosterDetail, PosterList

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', about, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^product/$', product, name='product'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^withyou/$', withyou, name='withyou'),
    url(r'^license/$', license, name='license'),
    url(r'^privacy/$', privacy, name='privacy'),

    # for resume
    url(r'^resume/$', ResumeList.as_view(), name='resume_list'),
    url(r'^resume/new/$', ResumeAdd.as_view(), name='resume_add'),
    url(r'^resume/(?P<slug>\w+)/$', ResumeDetail.as_view(), name='resume_detail'),
    url(r'^resume/(?P<slug>\w+)/update/$', ResumeUpdate.as_view(), name='resume_update'),
    url(r'^resume/(?P<slug>\w+)/delete/$', ResumeDelete.as_view(), name='resume_delete'),
    url(r'^resume/(?P<slug>\w+)/inform/$', resume_inform, name='resume_inform'),

    url(r'^resume/(?P<slug>\w+)/review/$', ResumeReviewAdd.as_view(), name='resumereview_add'),
    url(r'^resume/review/(?P<pk>\d+)/$', ResumeReviewUpdate.as_view(), name='resumereview_update'),
    url(r'^resume/review/(?P<pk>\d+)/delete/$', ResumeReviewDelete.as_view(), name='resumereview_delete'),

    # for poster
    url(r'^poster/$', PosterList.as_view(), name='poster_list'),
    url(r'^poster/(?P<pk>\d+)/$', PosterDetail.as_view(), name='poster'),

    # for testimonial
    url(r'^testimonial/(?P<pk>\d+)/$', TestimonialDetail.as_view(), name='testimonial'),

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
