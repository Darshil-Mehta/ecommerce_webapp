from django.db import models
from .customer import Customer
from .product import Product

class Feedback(models.Model):
    problem_issue = models.TextField(max_length=256, default='')
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_issue = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    feedback_image = models.FileField(default="no_img.png", upload_to='feedback_images')