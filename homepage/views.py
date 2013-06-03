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
