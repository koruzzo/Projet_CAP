# Generated by Django 5.0.2 on 2024-03-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_f_vaccin_nb_doses_alter_f_vaccin_nb_ucd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d_localisation',
            name='code_region',
            field=models.CharField(max_length=4),
        ),
    ]