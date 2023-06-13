from django.db import models
from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=150)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item_name
