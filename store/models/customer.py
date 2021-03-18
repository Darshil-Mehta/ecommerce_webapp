from django.db import models

class Customer(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField(default='')
    contact_no = models.CharField(max_length=15)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.email

    def register(self):
        self.save()
    
    def isEmailUsed(self):
        if Customer.objects.filter(email= self.email):
            return True
        return False
    
    def isContactUsed(self):
        if Customer.objects.filter(contact_no= self.contact_no):
            return True
        return False

    @staticmethod
    def getAddressByEmail(email):
        try:
            return Customer.objects.filter(email=email).first().address
        except:
            return ''

    @staticmethod
    def getCustomerByEmail(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False