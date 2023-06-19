from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import *
from .models import Cart, CartItem
from item.models import Category, Item
from .forms import LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from notifications.signals import notify

def logout_req(request):
    logout(request)
    return redirect("base:index")
# Create your views here.
def index(request):
    categories = Category.objects.all()
    items = Item.objects.all()

    return render(request, 'base/index.html', {
        'categories': categories,
        'items': items,
    })

def add_item(request,item_id):
    item = Item.objects.get(id=item_id)
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.get(customer=customer)
    if cart:
        CartItem.objects.create(cart=cart,product=item,quantity=1)
        
    else:
        cart = Cart.objects.create(customer=customer)
        CartItem.objects.create(cart=cart,product=item,quantity=1)
    messages.success(request, 'Added to cart')
    return redirect('base:index')

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

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("base:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="base/login.html", context={"login_form":form})

def add_to_cart(request):
    if request.user.is_authenticated:
        customer, created= Customer.objects.get_or_create(user=request.user)
        
        cart, created = Cart.objects.get_or_create(customer=customer)
        if request.method == 'POST':
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))

            product = Item.objects.get(id=product_id)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            cart_item.quantity += quantity
            cart_item.save()

            return redirect('base:shopping_cart')

        else:
            items = cart.items.all()

    else:
        items = []
        return redirect('/login')

    context = {'items': items}
    return render(request, 'base/shopping_cart.html', context)

def profile(request):
    return render(request, 'base/profile.html')
