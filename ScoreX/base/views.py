from django.shortcuts import render
from .forms import SignupForm
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

def signup(request):
    form = SignupForm()
    return render(request, 'base/signup.html', {
        'form': form

    })
def add_to_cart(request):
    return render(request, 'base/shopping_cart.html')