from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    patronymic = forms.CharField(max_length=50)
    balance = forms.DecimalField(max_digits=10, decimal_places=2)
    document_image = forms.ImageField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'first_name', 'last_name', 'patronymic', 'balance', 'document_image', 'password1', 'password2')
