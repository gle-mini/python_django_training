from django.urls import path
from . import views

urlpatterns = [
    path('django/', views.django_intro, name='django_intro'),
    path('display/', views.display_page, name='display_page'),
    path('templates/', views.template_engine, name='template_engine'),
]

