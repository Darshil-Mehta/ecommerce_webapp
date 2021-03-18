from django.db import models
from datetime import datetime
from .product import Product
from .customer import Customer

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(default=datetime.today)
    address = models.TextField(default='')
    phone = models.CharField(max_length=15, default='')

    def PlaceOrder(self):
        self.save()