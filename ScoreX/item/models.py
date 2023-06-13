from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    
