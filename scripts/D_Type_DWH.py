import sqlite3
from collections import defaultdict
import pandas as pd
from api.models import D_Type

def run():
    """Importe les données date de la table ODS dans le modèle D_Date."""
    conn = sqlite3.connect('db.sqlite3')
    
    df_date = pd.read_sql_query("SELECT type_de_vaccin FROM app_vaccination", conn)
    dates_to_create = defaultdict(list)
    
    for _, row in df_date.iterrows():
        type_vac = row['type_de_vaccin']
        
        if type_vac not in dates_to_create:
            dates_to_create[type_vac] = D_Type(
                type_vac = type_vac
            )
    
    D_Type.objects.bulk_create(dates_to_create.values())
    
    conn.close()