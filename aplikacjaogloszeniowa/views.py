from django.shortcuts import render

from .models import Kategoria


def index(request):
    kategorie = Kategoria.objects.all()
    context = {
        'kategorie': kategorie,
    }
    return render(request,'aplikacjaogloszeniowa/index.html',context)
