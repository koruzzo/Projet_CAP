"""..."""
from django.db import models

class Vaccination(models.Model):
    """Model de l'ODS du flux-total-dep.csv"""
    code_region = models.CharField(max_length=255)
    libelle_region = models.CharField(max_length=255)
    code_departement = models.CharField(max_length=255)
    libelle_departement = models.CharField(max_length=255)
    date_fin_semaine = models.CharField(max_length=255)
    type_de_vaccin = models.CharField(max_length=255)
    nb_ucd = models.CharField(max_length=255)
    nb_doses = models.CharField(max_length=255)
    def __str__(self):
        """..."""
        return f"{self.code_region} - {self.code_departement} - {self.type_de_vaccin} - {self.type_de_vaccin}"
