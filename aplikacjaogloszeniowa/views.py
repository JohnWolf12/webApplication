from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import Kategoria


def index(request):
    kategorie = Kategoria.objects.all()
    context = {
        'kategorie': kategorie,
    }
    return render(request, 'aplikacjaogloszeniowa/index.html', context)


def register_view(request):
    if request.method == 'POST':
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            return HttpResponseRedirect("/")
    else:
        registerform = RegisterForm()
    context = {
        'registerform': registerform
    }
    return render(request, 'aplikacjaogloszeniowa/register.html', context)


def logout_view(request):
    logout(request)
    return redirect("/")
