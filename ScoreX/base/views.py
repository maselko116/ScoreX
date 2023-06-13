from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect('/login')
    else:
        form = SignupForm()
    return render(request, 'base/signup.html', {
        'form': form

    })
def add_to_cart(request, item_id):
    if request.user.is_authenticated:
        try:
            item = Item.objects.get(id=item_id)
            request.user.cart_items.add(item)
        except Item.DoesNotExist:
            return render(request, 'base/error.html', {'error_message': 'Item does not exist.'})
    else:
        return redirect('/login')
    
    return render(request, 'base/shopping_cart.html', {'item': item})


 
