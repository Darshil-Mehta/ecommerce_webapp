from django.shortcuts import render
from .models.product import Product

def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store/home.html', context)