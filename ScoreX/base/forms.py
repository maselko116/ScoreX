from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'my-input', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'my-input', 'placeholder': 'Password'}))



class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password1')
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'my-input', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'my-input', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'my-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'my-input', 'placeholder': 'Confirm Password'}))