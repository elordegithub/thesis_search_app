# thesisapp/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Thesis

def landing_page(request):
    return render(request, 'thesis_search/landing.html')

def thesis_list(request):
    theses = Thesis.objects.all()[:3]  # Get the first three thesis studies
    return render(request, 'thesis_search/thesis_list.html', {'theses': theses})

def search_results(request):
    query = request.GET.get('q')
    if query:
        theses = Thesis.objects.filter(title__icontains=query) | \
                 Thesis.objects.filter(author__icontains=query) | \
                 Thesis.objects.filter(abstract__icontains=query)
    else:
        theses = []
    return render(request, 'thesis_search/search_results.html', {'theses': theses})
