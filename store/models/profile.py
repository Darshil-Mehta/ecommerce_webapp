from django.db import models
from .customer import Customer
from PIL import Image

class Profile(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='profile_pics')

    def __str__(self):
        return f"{self.customer.email}'s Profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            ouput_size = (300, 300)
            img.thumbnail(ouput_size)
            img.save(self.image.path)