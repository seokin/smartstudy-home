from django import http
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils.http import is_safe_url
from django.utils.translation import check_for_language
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Crew, App, Resume, Job
from .forms import ResumeForm


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


def robots(request):
    return render(request, 'robots.txt', content_type='text/plain')


def takeride(request):
    jobs = Job.objects.filter(active=True)
    return render(request, 'jobs.html', {
        'jobs': jobs,
    })


class resume_add(CreateView):
    model = Resume
    form_class = ResumeForm
    slug_field = 'hash_code'
    template_name_suffix = '_add'

    def get_initial(self):
        return {'apply_to': self.request.GET.get('job')}

    def get_success_url(self):
        return reverse_lazy('resume_detail', args=(self.object.hash_code,))


class resume_detail(DetailView):
    model = Resume
    slug_field = 'hash_code'


class resume_update(UpdateView):
    model = Resume
    form_class = ResumeForm
    slug_field = 'hash_code'
    template_name_suffix = '_update'

    def get_initial(self):
        initial = {}
        for k in self.model._jsonfields().iterkeys():
            initial[k] = self.object.desc.get(k)

        return initial

    def get_success_url(self):
        return reverse_lazy('resume_detail', args=(self.object.hash_code,))


class resume_delete(DeleteView):
    model = Resume
    forms = ResumeForm
    slug_field = 'hash_code'
    template_name_suffix = '_delete'
    success_url = reverse_lazy('takeride')
