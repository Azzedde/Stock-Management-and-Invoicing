# Generated by Django 3.2.9 on 2021-12-18 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0012_remove_etablissement_etat'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleBL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantité', models.IntegerField(null=True)),
                ('Article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Gestion.article')),
            ],
        ),
        migrations.AlterField(
            model_name='bon',
            name='Articles',
            field=models.ManyToManyField(to='Gestion.ArticleBL'),
        ),
    ]
