from django.urls import path
from django.contrib.auth import views as auth_views
import notifications.urls
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_req, name='logout'),
    path('add_item/<int:item_id>/',views.add_item,name='add_item'),
    path('shopping_cart/', views.go_to_cart, name='go_to_cart'),
    path('sending_data/', views.sending_data, name='sending_data'),
    path('signup/', views.signup, name='signup'),

    #path('shopping_cart/', views.add_to_cart, name='add_to_cart'),
    #path('login/', auth_views.LoginView.as_view(template_name='base/login.html', authentication_form=LoginForm), name = 'login'),
]