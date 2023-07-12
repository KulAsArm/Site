from django.urls import path
from . import views


urlpatterns = [path('', views.index, name='base'),
               path('booking/', views.booking, name='booking'),
               path('aboutus/', views.aboutus, name='aboutus'),
               path('dest/', views.dest, name='dest')]
