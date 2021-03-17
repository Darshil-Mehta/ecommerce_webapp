from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password

# -products- stores all the products 
# -categories- stores all the catergories from the database
# -cid- gets the current category id and calls its respective products

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

def register(request):
    if request.method == 'GET':
        return render(request, 'store/register.html')
    else:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        curr_values = {
            'fname': fname,
            'lname': lname,
            'email': email,
            'phone': phone,
        }
        customer = Customer(fname= fname, lname= lname, email= email, contact_no= phone, password= password)
        em = None
        if not fname:
            em = 'Firstname field required!'
        elif len(fname) < 4:
            em = 'Length of firstname should be greater than 4 letters'
        elif not lname:
            em = 'Lastname field required!'
        elif len(lname) < 4:
            em = 'Length of lastname should be greater than 4 letters'
        elif not phone:
            em = 'Contact number field required!'
        elif len(phone) != 10:
            em = 'Contact number should have 10 digits'
        elif not password:
            em = 'Please enter a secured password!'
        elif len(password) < 4:
            em = 'Password length should be atleast 4 character long!'
        elif customer.isEmailUsed():
            em = 'Email ID is already registered! Please try to login.'
        elif customer.isContactUsed():
            em = 'Contact Number is already used! Please use other contact number.'    
        if not em:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('store-home')
        else:
            data = {
                'error': em,
                'values': curr_values
            }
            return render(request, 'store/register.html', data)