from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, UpdateUserForm, UpdateUzytkownikForm, AnnouncementForm
from .models import Kategoria, Ogloszenie


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
            return redirect("/logowanie")
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
    uzytkownik = request.user.uzytkownik
    ogloszenia = Ogloszenie.objects.filter(uzytkownik=uzytkownik)
    context = {
        'ogloszenia': ogloszenia
    }
    return render(request, 'aplikacjaogloszeniowa/profile.html', context)


@login_required
def profileEdit_view(request):
    if request.method == 'POST':
        userform = UpdateUserForm(request.POST, instance=request.user)
        uzytkownikform = UpdateUzytkownikForm(request.POST, instance=request.user.uzytkownik)
        if userform.is_valid() and uzytkownikform.is_valid():
            userform.save()
            uzytkownikform.save()
            return redirect("/profil")
    else:
        userform = UpdateUserForm(instance=request.user)
        uzytkownikform = UpdateUzytkownikForm(instance=request.user.uzytkownik)
    context = {
        'userform': userform,
        'uzytkownikform': uzytkownikform
    }
    return render(request, 'aplikacjaogloszeniowa/profileEdit.html', context)


@login_required
def addAnnouncement_view(request):
    if request.method == 'POST':
        addannouncementform = AnnouncementForm(request.POST)
        addannouncementform.instance.uzytkownik = request.user.uzytkownik
        if addannouncementform.is_valid():
            addannouncementform.save()
            return redirect("/profil")
    else:
        addannouncementform = AnnouncementForm()
    context = {
        'addannouncementform': addannouncementform
    }
    return render(request, 'aplikacjaogloszeniowa/announcementAdd.html', context)


@login_required
def editAnnouncement_view(request, id):
    ogloszenie = get_object_or_404(Ogloszenie, pk=id, uzytkownik=request.user.uzytkownik)
    if request.method == 'POST':
        editannouncementform = AnnouncementForm(request.POST, instance=ogloszenie)
        if editannouncementform.is_valid():
            editannouncementform.save()
            return redirect("/profil")
    else:
        editannouncementform = AnnouncementForm(instance=ogloszenie)
    context = {
        'editannouncementform': editannouncementform
    }
    return render(request, 'aplikacjaogloszeniowa/announcementEdit.html', context)


@login_required
def deleteAnnouncement_view(request, id):
    uzytkownik = request.user.uzytkownik
    Ogloszenie.objects.filter(uzytkownik=uzytkownik, id=id).delete()
    return redirect('/profil')


def announcement_view(request):
    nazwa = request.GET.get("q")
    kategoria = request.GET.get("k")
    if kategoria == '0':
        ogloszenia = Ogloszenie.objects.filter(nazwa__icontains=nazwa)
    else:
        ogloszenia = Ogloszenie.objects.filter(kategoria_id=kategoria, nazwa__icontains=nazwa)
    paginator = Paginator(ogloszenia, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "nazwa": nazwa,
        "kategoria": kategoria,
        "page_obj": page_obj
    }
    return render(request, 'aplikacjaogloszeniowa/announcement.html', context)
