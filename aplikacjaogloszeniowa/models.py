from django.db import models
from django.contrib.auth.models import User


class Uzytkownik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=9)
    miejscowosc = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "użytkownik"
        verbose_name_plural = "użytkownicy"


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "kategoria"
        verbose_name_plural = "kategorie"


class Podkategoria(models.Model):
    nazwa = models.CharField(max_length=50)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "podkategoria"
        verbose_name_plural = "podkategorie"


class Ogloszenie(models.Model):
    nazwa = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=9, decimal_places=2)
    opis = models.TextField(blank=True, max_length=1000)
    podkategoria = models.ForeignKey(Podkategoria, on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "ogłoszenie"
        verbose_name_plural = "ogłoszenia"


class Zdjecie(models.Model):
    zdjecie = models.ImageField()
    ogloszenie = models.ForeignKey(Ogloszenie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.zdjecie)

    class Meta:
        verbose_name = "zdjęcie"
        verbose_name_plural = "zdjęcia"
