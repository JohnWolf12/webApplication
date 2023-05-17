from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Nazwa użytkownika', widget=forms.TextInput(
        attrs={
            'class': 'form-control bg-light'
        }
    ))
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control bg-light'
        }
    ))
    password2 = forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control bg-light'
        }
    ))
    email = forms.EmailField(label='Adres e-mail', widget=forms.EmailInput(
        attrs={
            'class': 'form-control bg-light'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
