import sqlite3
import pandas as pd
from datetime import datetime

from django.utils.text import slugify
from api.models import F_Vaccin, D_Localisation, D_Date, D_Type

def run():
    conn = sqlite3.connect('db.sqlite3')
    
    df_vaccin = pd.read_sql_query("SELECT code_region, code_departement, date_fin_semaine, type_de_vaccin, nb_ucd, nb_doses FROM app_vaccination WHERE nb_ucd != 'nan' AND nb_doses != 'nan'", conn)
    conn.close()

    vaccins_to_create = {}
    
    localisations_dict = {f"{loc.code_region}-{loc.code_depart}": loc for loc in D_Localisation.objects.all()}
    dates_dict = {date.date_fs: date for date in D_Date.objects.all()}
    types_dict = {type_vac.type_vac: type_vac for type_vac in D_Type.objects.all()}
    
    for _, row in df_vaccin.iterrows():
        code_region, code_departement, date_fin_semaine, type_de_vaccin, nb_ucd, nb_doses = row
        date_fin_semaine = datetime.strptime(date_fin_semaine, '%Y-%m-%d').date()
        if len(code_region) == 1:
            code_region = f"0{code_region}"
        if len(code_departement) == 1:
            code_departement = f"0{code_departement}"
        id_vac = slugify(f"{code_region}-{code_departement}-{date_fin_semaine}-{type_de_vaccin}")
        
        if id_vac not in vaccins_to_create:
            try:
                localisation = localisations_dict[f"{code_region}-{code_departement}"]
            except KeyError:
                print("Localisation non trouvée pour:", f"{code_region}-{code_departement}")
                localisation = None

            try:
                date = dates_dict[date_fin_semaine]
            except KeyError:
                print("Date non trouvée pour:", date_fin_semaine)
                date = None

            try:
                type_vaccin = types_dict[type_de_vaccin]
            except KeyError:
                print("Type de vaccin non trouvé pour:", type_de_vaccin)
                type_vaccin = None

            if localisation and date and type_vaccin:
                vaccins_to_create[id_vac] = F_Vaccin(
                    id_vac=id_vac,
                    local_fk=localisation,
                    date_fk=date,
                    type_fk=type_vaccin,
                    nb_ucd=nb_ucd,
                    nb_doses=nb_doses
                )
            else:
                print("Une ou plusieurs clés étrangères n'ont pas été trouvées.")
        elif float(nb_doses) > 0:
            existing_vaccin = vaccins_to_create[id_vac]
            existing_nb_doses = existing_vaccin.nb_doses
            existing_vaccin.nb_doses = float(nb_doses)
            existing_vaccin.nb_ucd = nb_ucd
            print(f"Remplacement de l'entrée pour {id_vac}. Ancien nombre de doses : {existing_nb_doses}. Nouveau nombre de doses : {nb_doses}.")
        else:
            print("Le vaccin avec cet ID existe déjà dans la liste des vaccins à créer :",id_vac)
    print("Nombre de vaccins à créer:", len(vaccins_to_create))
    F_Vaccin.objects.bulk_create(vaccins_to_create.values())
    print("BDD remplie !")
