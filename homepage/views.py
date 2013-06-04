from django.shortcuts import render
from .models import Crew, App


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
