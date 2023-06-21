from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import *
from .forms import LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Order_Details
from notifications.signals import notify

from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from .forms import OrderDetailsForm



def logout_req(request):
    logout(request)
    return redirect("base:index")
# Create your views here.
def index(request):
    categories = Category.objects.all()
    items = Item.objects.all()  

    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
    })


def go_to_cart(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(customer=customer)
        items = CartItem.objects.filter(cart=cart)

        total_price = 0 

        if request.method == 'POST':
            
            order = Order.objects.create(customer=customer)
        
            if items:
                for item in items:
                    OrderItem.objects.create(product=item.product, order=order)
                    total_price += item.product.price * item.quantity  # Dodanie ceny produktu do łącznej ceny koszyka
                    item.delete()  # Usunięcie elementu koszyka
                cart.delete()  # Usunięcie koszyka
                return redirect('base:sending_data')
        
        # Obliczenie łącznej ceny koszyka
        for item in items:
            total_price += item.product.price * item.quantity
        
        context = {'items': items,
                'cart': cart,
                'total_price': total_price
                } 
        return render(request, 'shopping_cart.html', context)
    else:
         return redirect('/login')

@login_required
def add_item(request, item_id):
    
    product = Item.objects.get(id=item_id)
    customer = Customer.objects.get(user=request.user)
    cart, created = Cart.objects.get_or_create(customer=customer)
    
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        
        CartItem.objects.create(cart=cart, product=product, quantity=1)

    cart.update_total_price()
    messages.success(request, 'Added to cart')
    return redirect('base:index')


def style(request):
    return render(request, 'frame.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user,name=user.username,email=user.email)

            return redirect('/login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
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
	return render(request=request, template_name="login.html", context={"login_form":form})


def sending_data(request):
    order_details = Order_Details.objects.all()
    #order = OrderItem.objects.get(product=order) 
    #order_items = OrderItem.objects.filter(order_details=order)
    
    context = {
        
        'order_details': order_details,
        #'order_items': order_items,
    }
    return render(request, 'sending_data.html', context)


def sending_data(request):
    if request.method == 'POST':
        form = OrderDetailsForm(request.POST)
        if form.is_valid():
            order_details = form.save()
            # Wykonaj inne operacje, takie jak zapisanie przedmiotów zamówienia itp.
            return redirect('order_details', order_id=order_details.id)
    else:
        form = OrderDetailsForm()
    
    return render(request, 'sending_data.html', {'order_details_form': form})

