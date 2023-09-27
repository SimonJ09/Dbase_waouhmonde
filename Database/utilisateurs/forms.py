from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="Required. Enter a valid email address.")

    class Meta:
        model = CustomUser
        fields = ['username','email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(max_length=254, help_text="Required. Enter a valid email address.")
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
