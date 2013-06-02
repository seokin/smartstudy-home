from django.shortcuts import render
from .models import Crew


def about(request):
    crew = Crew.objects.all()
    return render(request, 'about.html', {
        'crew': crew,
    })


def product(request):
    return render(request, 'product.html')


def contact(request):
    return render(request, 'contact.html')
