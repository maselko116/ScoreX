from django.db import models
from django.contrib.auth.models import User
from item.models import *
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name}"



class Order_Details(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True, null=True)

    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    
    #status = models.Booleanfield (default=False, null=True, blank=True)
    
    def __str__(self):
        return self.address 
    