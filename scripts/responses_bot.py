# responses_bot.py

from random import choice
from django.db.models import Sum
from django.utils.timezone import now
from asgiref.sync import sync_to_async
from api.models import F_Vaccin
from datetime import timedelta


def get_total_vaccine_doses():
    date_n_3_years_ago = now() - timedelta(weeks=3*52)
    sunday_of_next_week = date_n_3_years_ago - timedelta(days=date_n_3_years_ago.weekday() + 1) + timedelta(weeks=1)
    total_doses = F_Vaccin.objects.filter(date_fk=sunday_of_next_week, local_fk__code_region='84', nb_doses__gt=0, local_fk__libelle_depart='Puy-de-Dôme').aggregate(Sum('nb_doses'))['nb_doses__sum'] or 0
    return total_doses
@sync_to_async
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Message vide.'
    elif 'affiche_vac' in lowered:
        total_doses = get_total_vaccine_doses()
        return f"Nombre total de doses de vaccin : {total_doses} et le lien GitHub : https://github.com/koruzzo/Projet_CAP"
    else:
        return choice(['Pas compris...',
                       'Nop rien compris...',
                       'Commande inconnue...'])
