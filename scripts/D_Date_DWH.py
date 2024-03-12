import sqlite3
from collections import defaultdict
import pandas as pd
from api.models import D_Date

def run():
    """Importe les données date de la table ODS dans le modèle D_Date."""
    conn = sqlite3.connect('db.sqlite3')
    
    df_date = pd.read_sql_query("SELECT date_fin_semaine FROM app_vaccination", conn)
    dates_to_create = defaultdict(list)
    
    for _, row in df_date.iterrows():
        date_fs = row['date_fin_semaine']
        
        if date_fs not in dates_to_create:
            dates_to_create[date_fs] = D_Date(
                date_fs = date_fs
            )
    
    D_Date.objects.bulk_create(dates_to_create.values())
    
    conn.close()