from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from app import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('home/', views.home, name='home'),
    path('', views.landing_redirect, name='landing_redirect'),
]