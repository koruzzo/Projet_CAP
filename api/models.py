from django.db import models
from django.utils.text import slugify


class D_Type(models.Model):
    """Table de dimension pour les types."""
    type_vac = models.CharField(primary_key=True, max_length=25)
    def __str__(self):
        """..."""
        return f"{self.type_vac}"

class D_Date(models.Model):
    """Table de dimension pour les dates."""
    date_fs = models.DateField(primary_key=True)
    def __str__(self):
        """..."""
        return f"{self.date_fs}"

class D_Localisation(models.Model):
    """Table de dimension pour la localisation."""
    id_local = models.SlugField(primary_key=True, max_length=9)
    code_region = models.CharField(max_length=4)
    code_depart = models.CharField(max_length=4)
    libelle_region = models.CharField(max_length=4)
    libelle_depart = models.CharField(max_length=30)
    def save(self, *args, **kwargs):
        self.id_local = slugify(f"{self.code_region}-{self.code_depart}")
        super().save(*args, **kwargs)
    def __str__(self):
        """..."""
        return f"{self.id_local} - {self.code_region} - {self.code_depart} - {self.libelle_region} - {self.libelle_depart}"

class F_Vaccin(models.Model):
    """Table de fait pour les vaccins."""
    id_vac = models.SlugField(primary_key=True, max_length=50)
    local_fk = models.ForeignKey('D_Localisation', on_delete=models.CASCADE)
    date_fk = models.ForeignKey('D_Date', on_delete=models.CASCADE)
    type_fk = models.ForeignKey('D_Type', on_delete=models.CASCADE)
    nb_ucd = models.FloatField()
    nb_doses = models.FloatField()
    def save(self, *args, **kwargs):
        self.id_vac = slugify(f"{self.local_fk}-{self.date_fk}-{self.type_fk}")
        super().save(*args, **kwargs)
    def __str__(self):
        """..."""
        return f"{self.id_vac} - {self.local_fk} - {self.date_fk} - {self.type_fk} -  {self.nb_ucd} - {self.nb_doses}"
