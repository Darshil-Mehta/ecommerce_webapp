from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('cart/', views.cart, name='store-cart'),
    path('checkout/', views.checkout, name='store-checkout'),
    path('orders/', views.orderview, name='store-orders-view'),
    path('profile/', views.profile, name='customer-profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('feedback/', views.feedback, name='feedback'),
    path('pay-here/', views.payment, name='payment')
]