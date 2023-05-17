# Generated by Django 4.1.7 on 2023-05-17 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacjaogloszeniowa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategoria',
            options={'verbose_name': 'kategoria', 'verbose_name_plural': 'kategorie'},
        ),
        migrations.AlterModelOptions(
            name='ogloszenie',
            options={'verbose_name': 'ogłoszenie', 'verbose_name_plural': 'ogłoszenia'},
        ),
        migrations.AlterModelOptions(
            name='podkategoria',
            options={'verbose_name': 'podkategoria', 'verbose_name_plural': 'podkategorie'},
        ),
        migrations.AlterModelOptions(
            name='uzytkownik',
            options={'verbose_name': 'użytkownik', 'verbose_name_plural': 'użytkownicy'},
        ),
        migrations.AlterModelOptions(
            name='zdjecie',
            options={'verbose_name': 'zdjęcie', 'verbose_name_plural': 'zdjęcia'},
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='miejscowosc',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='uzytkownik',
            name='telefon',
            field=models.CharField(blank=True, max_length=9),
        ),
    ]