from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_finance', views.add_finance, name='add_finance'),
    path('login', views.signin_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('delete', views.delete, name='delete'),
]
