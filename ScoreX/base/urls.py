from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'), 
    path('shopping_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),

    #path('shopping_cart/', views.add_to_cart, name='add_to_cart'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html', authentication_form=LoginForm), name = 'login'),
]