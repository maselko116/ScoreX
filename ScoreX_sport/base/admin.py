from django.contrib import admin

from .models import *
# Registered models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Order_Details)
admin.site.register(Cart)
admin.site.register(CartItem)
# Registered items here.
admin.site.register(Category)
admin.site.register(Item)
