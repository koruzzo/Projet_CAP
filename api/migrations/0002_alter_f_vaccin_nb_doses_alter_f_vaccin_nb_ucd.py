# Generated by Django 5.0.2 on 2024-02-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f_vaccin',
            name='nb_doses',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name='f_vaccin',
            name='nb_ucd',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]