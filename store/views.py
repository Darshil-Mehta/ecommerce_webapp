from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.profile import Profile
from .models.orders import Order
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    if request.method == 'GET':
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
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
    else:
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('store-home')

def register(request):
    if request.method == 'GET':
        return render(request, 'store/register.html')
    else:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        curr_values = {
            'fname': fname,
            'lname': lname,
            'email': email,
            'phone': phone,
            'address': address
        }
        customer = Customer(fname= fname, lname= lname, email= email, contact_no= phone, password= password, address= address)
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
        elif len(address) < 10:
            em = 'Please mention that acturate address with atleast 10 characters'
        elif customer.isEmailUsed():
            em = 'Email ID is already registered! Please try to login.'
        elif customer.isContactUsed():
            em = 'Contact Number is already used! Please use other contact number.'    
        if not em:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': em,
                'values': curr_values
            }
            return render(request, 'store/register.html', data)

def login(request):
    if request.method == 'GET':
        return render(request, 'store/login.html')
    else:
        error_msg = None
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.getCustomerByEmail(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                return redirect('store-home')
            else:
                error_msg = 'Invalid password for the mentioned EmailID'
        else:
            error_msg = 'EmailID is not registered! Please register on the website!'
        data = {
            'error': error_msg,
        }
        return render(request, 'store/login.html', data)

def logout(request):
    request.session.clear()
    return redirect('login')

def cart(request):
    ids = list(request.session.get('cart').keys())
    cartdata = Product.get_products_for_cart(ids)
    data = {
        'cartdata': cartdata,
    }
    return render(request, 'store/cart.html', data)

def checkout(request):
    phone = request.POST.get('phone')
    customer_id = request.session.get('customer_id')
    email = request.session.get('customer_email')
    address = Customer.getAddressByEmail(email)
    cart = request.session.get('cart')
    products = Product.get_products_for_cart(list(cart.keys()))
    for product in products:
        p = product.price
        q = cart.get(str(product.id))
        order = Order(product= product, customer= Customer(id= customer_id), quantity= q, price= p*q, address= address, phone= phone)
        order.PlaceOrder()
        request.session['cart'] = {}
    return redirect('store-cart')

def orderview(request):
    id = request.session.get('customer_id')
    all_orders = Order.getAllOrdersByID(id)
    data = {
        'allorders': all_orders,
    }
    return render(request, 'store/orders.html', data)

def profile(request):
    if request.method == 'GET':
        customer_email = request.session.get('customer_email')
        cid = request.session.get('customer_id')
        user = Customer.objects.filter(email=customer_email).first()
        profile = Profile.objects.filter(customer=cid).first()
        data = {
            'customer': user,
            'profile': profile,
        }
        return render(request, 'store/profile.html', data)
    else:
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        image = request.POST.get('profile')
        customer_email = request.session.get('customer_email')
        user = Customer.objects.filter(email=customer_email).first()
        if address:
            if len(address) > 10:
                user.address = address
                user.save()
        elif phone:
            if len(phone) == 10:
                user.contact_no = phone
                user.save()
        return redirect('customer-profile')