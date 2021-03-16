from django.shortcuts import render
from .models.product import Product
from .models.category import Category

def home(request):
    products = None
    categories = Category.get_all_categories()
    cid = request.GET.get('category')
    if cid:
        products = Product.get_products_by_id(cid)
    else:
        products = Product.get_all_products()
    data = {
        'products': products,
        'categories': categories, 
    }
    return render(request, 'store/home.html', data)