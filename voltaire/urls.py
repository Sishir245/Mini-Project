from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('appointment',views.appointment, name='appointment'),
    path('contact',views.contact, name='contact'),
    path('destination',views.destination, name='destination'),
    path('home',views.home, name='home'),
    path('login',views.login, name='login'),
    path('process',views.process, name='process'),
    path('register',views.register, name='register'),
    path('retry',views.retry, name='retry'),
    path('scholarship',views.scholarship, name='scholarship'),
    path('services',views.services, name='services'),
    path('test',views.test, name='test'),
    path('universities',views.universities, name='universities'),
]