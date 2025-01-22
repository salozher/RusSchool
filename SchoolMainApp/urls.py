from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from SchoolMainApp.views import (home_view, team_view, about_view, contact_view, news_view,)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', home_view, name='home'),
    path('team/', team_view, name='team'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_view, name='success'),
    path('news/', news_view, name='news'),
]
