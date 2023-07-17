from django.urls import path
from . import views


urlpatterns = [path('', views.index, name='base'),
               path('booking/', views.booking, name='booking'),
               path('booking2/', views.booking2, name='booking2'),
               path('booking3/', views.booking3, name='booking3'),
               path('booking4/', views.booking4, name='booking4'),
               path('booking5/', views.booking5, name='booking5'),
               path('booking6/', views.booking6, name='booking6'),
               path('booking7/', views.booking7, name='booking7'),
               path('booking8/', views.booking8, name='booking8'),
               path('aboutus/', views.aboutus, name='aboutus'),
               path('dest/', views.dest, name='dest')]
