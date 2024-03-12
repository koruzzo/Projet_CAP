import sqlite3
import pandas as pd
from django.utils.text import slugify
from api.models import D_Localisation

def run():
    """Importe les données de localisation de la table ODS dans le modèle D_Localisation."""
    conn = sqlite3.connect('db.sqlite3')

    df_localisation = pd.read_sql_query("SELECT code_region, libelle_region, code_departement, libelle_departement FROM app_vaccination", conn)

    conn.close()

    localisations_to_create = {}

    for _, row in df_localisation.iterrows():
        code_region, libelle_region, code_departement, libelle_departement = row
        if len(code_region) == 1:
            code_region = f"0{code_region}"
        if len(code_departement) == 1:
            code_departement = f"0{code_departement}"
        id_local = slugify(f"{code_region}-{code_departement}")

        if id_local not in localisations_to_create:
            localisations_to_create[id_local] = D_Localisation(
                id_local=id_local,
                code_region=code_region,
                libelle_region=libelle_region,
                code_depart=code_departement,
                libelle_depart=libelle_departement
            )
    print("Nombre de localisation à créer:", len(localisations_to_create))
    D_Localisation.objects.bulk_create(localisations_to_create.values())
    print("BDD remplie !")
