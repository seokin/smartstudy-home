from django import http
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.db.models import Avg, Count
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.utils.translation import check_for_language
from django.http import Http404
#from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Crew, App, Resume, Job, Testimonial, Poster, ResumeReview
from .forms import ResumeForm, ResumeReviewForm
from .helper import sendResumeLink


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
    jobs = Job.objects.filter(active=True)
    testimonials = Testimonial.objects.all()
    return render(request, 'withyou.html', {
        'jobs': jobs,
        'testimonials': testimonials,
    })


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


class ResumeEditMixin(object):
    model = Resume
    form_class = ResumeForm
    slug_field = 'uuid'
    template_name_suffix = '_edit'

    def get_initial(self):
        initial = {}

        if self.object:
            for k in self.model.descfields().iterkeys():
                initial[k] = self.object.desc.get(k)
        else:
            initial['apply_to'] = self.request.GET.get('job')

        return initial

    def form_valid(self, form):
        # Which submit button had been chosen?
        if self.request.POST.get('draft'):
            form.instance.status = Resume.DRAFT
        elif self.request.POST.get('submit'):
            form.instance.status = Resume.SUBMIT

        # Put data into jsonfield
        for k, v in self.model.descfields().iteritems():
            form.instance.desc[k] = self.request.POST.get(k)
        return super(ResumeEditMixin, self).form_valid(form)


class ResumeAdd(ResumeEditMixin, CreateView):
    def get_success_url(self):
        #sendResumeLink(request, self.object)
        return reverse_lazy('resume_inform', args=(self.object.uuid,))


class ResumeUpdate(ResumeEditMixin, UpdateView):
    def get_object(self, *args, **kwargs):
        obj = super(ResumeUpdate, self).get_object(*args, **kwargs)
        if not obj.in_draft():
            raise Http404
        return obj


class ResumeList(ListView):
    paginate_by = 50

    @method_decorator(permission_required('homepage.change_resume'))
    def dispatch(self, *args, **kwargs):
        return super(ResumeList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = Resume.objects.all().annotate(
            avg_rating=Avg('resumereview__rating'),
            review_count=Count('resumereview__rating')
        )
        sort = self.request.GET.get('sort', '-modified')
        if sort:
            queryset = queryset.order_by(sort)

        if self.request.GET.get('job'):
            queryset = queryset.filter(apply_to=int(self.request.GET.get('job')))

        for resume in queryset:
            resume.reviewed = ResumeReview.objects.filter(user=self.request.user, resume=resume).exists()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ResumeList, self).get_context_data(**kwargs)
        context['table'] = [
            ('name', 'Name'),
            ('email', 'Email'),
            ('status', 'Status'),
            ('apply_to', 'Apply to'),
            ('avg_rating', 'Rating'),
            ('review_count', 'Review'),
            ('modified', 'Last update'),
        ]
        context['user'] = self.request.user
        context['sort'] = self.request.GET.get('sort')
        context['job'] = int(self.request.GET.get('job', 0))
        context['jobs'] = Job.objects.all()
        return context


class ResumeDetail(DetailView):
    model = Resume
    slug_field = 'uuid'


class ResumeDelete(DeleteView):
    model = Resume
    forms = ResumeForm
    slug_field = 'uuid'
    template_name_suffix = '_delete'
    success_url = reverse_lazy('index')


def resume_inform(request, slug):
    resume = get_object_or_404(Resume, uuid=slug)
    sendResumeLink(request, resume)

    return render(request, 'homepage/resume_inform.html', {
        'resume': resume,
    })


class TestimonialDetail(DetailView):
    model = Testimonial


class PosterDetail(DetailView):
    model = Poster


class PosterList(ListView):
    model = Poster


class ResumeReviewAdd(CreateView):
    model = ResumeReview
    form_class = ResumeReviewForm
    template_name_suffix = '_edit'

    @method_decorator(permission_required('homepage.add_resumereview'))
    def dispatch(self, *args, **kwargs):
        return super(ResumeReviewAdd, self).dispatch(*args, **kwargs)

    def get_initial(self):
        initial = {
            'resume': Resume.objects.get(uuid=self.kwargs['slug']),
            'user': self.request.user,
        }
        return initial

    def get_success_url(self):
        return reverse_lazy('resume_detail', args=(self.object.resume.uuid,))


class ResumeReviewUpdate(UpdateView):
    model = ResumeReview
    form_class = ResumeReviewForm
    template_name_suffix = '_edit'

    def get_object(self, *args, **kwargs):
        obj = super(ResumeReviewUpdate, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise Http404
        return obj

    def get_initial(self):
        initial = {
            'resume': self.object.resume,
            'user': self.object.user,
        }
        return initial

    def get_success_url(self):
        return reverse_lazy('resume_detail', args=(self.object.resume.uuid,))


class ResumeReviewDelete(DeleteView):
    model = ResumeReview
    forms = ResumeReviewForm
    template_name_suffix = '_delete'
    success_url = reverse_lazy('resume_list')

    def get_object(self, *args, **kwargs):
        obj = super(ResumeReviewDelete, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise Http404
        return obj
