import pandas as pd
from app.models import Vaccination
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def run():
    """Script d'insertion de données dans la table ODS Vaccination"""
    csv_file_path = os.path.join(DATA_DIR, 'flux-total-dep.csv')
    data = pd.read_csv(csv_file_path, sep=',',encoding='ISO-8859-1',dtype=str)
    data = data.to_dict(orient='records')
    data = [Vaccination(**row) for row in data]
    Vaccination.objects.bulk_create(data)
