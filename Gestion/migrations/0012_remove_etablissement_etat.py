# Generated by Django 3.2.9 on 2021-12-17 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0011_etablissement_etat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etablissement',
            name='Etat',
        ),
    ]
