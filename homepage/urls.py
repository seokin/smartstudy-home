from django.conf.urls import patterns, url, include
from django.conf import settings
from .views import about, product, contact, withyou, license, privacy

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
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^i18n/', include('django.conf.urls.i18n')),
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
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
