from django.shortcuts import render

from item.models import Category, Item
# Create your views here.
def index(request):
    categories = Category.objects.all()
    items = Item.objects.all()

    return render(request, 'base/index.html', {
        'categories': categories,
        'items': items,
    })
def style(request):
    return render(request, 'frame.html')