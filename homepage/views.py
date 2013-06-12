from django.shortcuts import render
from .models import Crew, App
from django import http
from django.conf import settings
from django.utils.translation import check_for_language
from django.utils.http import is_safe_url


def about(request):
    crew = Crew.objects.all()
    return render(request, 'about.html', {
        'crew': crew,
    })


def product(request):
    apps = App.objects.all()
    return render(request, 'product.html', {
        'apps': apps,
    })


def contact(request):
    return render(request, 'contact.html')


def withyou(request):
    return render(request, 'withyou.html')


def license(request):
    return render(request, 'license.html')


def privacy(request):
    return render(request, 'privacy.html')


def setlang(request, lang_code):
    # Copied from django.views.i18n.set_language
    next = request.REQUEST.get('next')
    if not is_safe_url(url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER')
        if not is_safe_url(url=next, host=request.get_host()):
            next = '/'
    response = http.HttpResponseRedirect(next)
    if lang_code and check_for_language(lang_code):
        if hasattr(request, 'session'):
            request.session['django_language'] = lang_code
        else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response
