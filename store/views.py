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
    if request.method == 'GET':
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
        print('email -> ',request.session.get('customer_email'))
        print('products -> ',product)
        cart = request.session.get('cart')
        if cart: # () if cart is presesnt
            quantity = cart.get(product) # get the quantity that user wants to buy
            if quantity: # (.) if the user has added that item into the cart
                if remove: # (..) check if user want to remove
                    if quantity <= 1: # (...) if product quantity less than 1 then remove item from cart
                        cart.pop(product) # else the quantity would be zero but it would still remain in cart
                    else: # (...) else just subtract the quantity by 1
                        cart[product] = quantity-1
                else: # (..) else the user wants to add
                    cart[product] = quantity+1
            else: # (.) else not then initialize the item by 1
                cart[product] = 1
        else: # () else make the user a new cart
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart ->',cart)
        return redirect('store-home')

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