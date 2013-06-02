from django.conf.urls import patterns, url, include
from django.conf import settings
from .views import about, product, contact

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', about, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^product/$', product, name='product'),
    url(r'^contact/$', contact, name='contact'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
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
