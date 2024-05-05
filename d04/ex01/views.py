from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def django_intro(request):
    return render(request, 'django_intro.html')

def display_page(request):
    return render(request, 'display_page.html')

def template_engine(request):
    return render(request, 'template_engine.html')

