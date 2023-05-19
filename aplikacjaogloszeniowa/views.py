from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateUserForm, UpdateUzytkownikForm
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


@login_required
def profile_view(request):
    return render(request, 'aplikacjaogloszeniowa/profile.html')


@login_required
def profileEdit_view(request):
    if request.method == 'POST':
        userform = UpdateUserForm(request.POST, instance=request.user)
        uzytkownikform = UpdateUzytkownikForm(request.POST, instance=request.user.uzytkownik)
        if userform.is_valid() and uzytkownikform.is_valid():
            userform.save()
            uzytkownikform.save()
            return HttpResponseRedirect("/profil")
    else:
        userform = UpdateUserForm(instance=request.user)
        uzytkownikform = UpdateUzytkownikForm(instance=request.user.uzytkownik)
    context = {
        'userform': userform,
        'uzytkownikform': uzytkownikform
    }
    return render(request, 'aplikacjaogloszeniowa/profileEdit.html', context)
