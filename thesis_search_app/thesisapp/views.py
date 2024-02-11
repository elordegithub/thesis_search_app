from django.shortcuts import render
from .models import Thesis

def thesis_search(request):
    query = request.GET.get('q')
    if query:
        theses = Thesis.objects.filter(title__icontains=query)
    else:
        theses = Thesis.objects.all()
    return render(request, 'thesis_search/search.html', {'theses': theses, 'query': query})
