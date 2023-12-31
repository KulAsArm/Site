from django.urls import path
from . import views


urlpatterns = [path('registration/', views.registration, name='registration'),
               path("login/",  views.user_login, name="login"),
               path('logout/', views.user_logout, name='logout'),
               path("profile/", views.user_profile, name="profile"),
               path("complited_profile/", views.user_complited_profile, name="complited_profile"),
               path('delete/', views.user_delete, name='delete'),
               path('delete_done/', views.user_delete_done, name='delete_done')]
