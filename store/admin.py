from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.profile import Profile
from .models.feedback import Feedback

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['fname','lname','address','email','contact_no']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product','quantity','price','status','customer','date']

class AdminFeedback(admin.ModelAdmin):
    list_display = ['customer','status','product_name','problem_issue','date_issue', 'feedback_image']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
admin.site.register(Profile)
admin.site.register(Feedback, AdminFeedback)