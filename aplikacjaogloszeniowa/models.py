from django.db import models
from django.contrib.auth.models import User


class Uzytkownik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=9)
    miejscowosc = models.CharField(max_length=50)


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50)


class Podkategoria(models.Model):
    nazwa = models.CharField(max_length=50)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)


class Ogloszenie(models.Model):
    nazwa = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=9, decimal_places=2)
    opis = models.TextField(blank=True, max_length=1000)
    podkategoria = models.ForeignKey(Podkategoria, on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)


class Zdjecie(models.Model):
    zdjecie = models.ImageField()
    ogloszenie = models.ForeignKey(Ogloszenie, on_delete=models.CASCADE)
