from django.urls import path
from . import views

urlpatterns = [
    path('', views.thesis_search, name='thesisapp'),
]

