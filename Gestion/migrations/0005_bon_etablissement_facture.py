# Generated by Django 3.2.9 on 2021-12-17 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0004_auto_20211214_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=100)),
                ('Montant', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num', models.IntegerField(null=True)),
                ('Articles', models.ManyToManyField(to='Gestion.Article')),
                ('Etab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.etablissement')),
            ],
        ),
        migrations.CreateModel(
            name='Bon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num', models.IntegerField(null=True)),
                ('Articles', models.ManyToManyField(to='Gestion.Article')),
                ('Etab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.etablissement')),
                ('Facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.facture')),
            ],
        ),
    ]