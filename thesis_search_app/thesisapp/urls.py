# thesisapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('thesis-list/', views.thesis_list, name='thesis_list'),
    path('search/', views.search_results, name='search_results'),
]