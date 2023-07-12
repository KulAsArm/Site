from django.urls import path
from . import views


urlpatterns = [path('registration/', views.registration, name='registration'),
               path("login/", views.user_login, name="login"),
               path("profile/", views.profile, name="profile")]