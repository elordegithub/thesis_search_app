from django.shortcuts import render
from .models import Thesis

def thesis_search(request):
    query = request.GET.get('q')
    theses = None
    if query:
        theses = Thesis.objects.filter(
            title__icontains=query
        ) | Thesis.objects.filter(
            author__icontains=query
        ) | Thesis.objects.filter(
            abstract__icontains=query
        )
    return render(request, 'thesis_search/search.html', {'theses': theses, 'query': query})