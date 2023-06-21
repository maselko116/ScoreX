from django.db import models
from django.contrib.auth.models import User
from .models import *

from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    total_price = models.FloatField(default=0)

    def update_total_price(self):
        items = self.items.all()
        total = sum(item.product.price * item.quantity for item in items)
        self.total_price = total
        self.save()


    def __str__(self):
        return f"Cart {self.id}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Item, on_delete=models.CASCADE,db_constraint=False )
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"CartItem {self.id}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"Cart {self.id}"
    

class Order_Details(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    #status = models.Booleanfield (default=False, null=True, blank=True)
    
    def __str__(self):
        return self.address    

class OrderItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order.customer} - {self.product}'