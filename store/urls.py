from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]