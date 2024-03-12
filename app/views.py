from datetime import date, timedelta
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Sum
from api.models import F_Vaccin


def index(request):
    """
    Affiche la page d'accueil avec les données sur les vaccins.
    
    Cette fonction récupère les données sur les vaccins pour la semaine à venir dans la région du Puy-de-Dôme,
    calcule le nombre total de doses de vaccin disponibles et les affiche sur la page d'accueil.
    
    Args:
        request: La requête HTTP reçue par la vue.

    Returns:
        HttpResponse: La réponse HTTP contenant la page d'accueil avec les données sur les vaccins.
    """
    date_n_3_years_ago = date.today() - timedelta(weeks=3*52)

    sunday_of_next_week = date_n_3_years_ago - timedelta(days=date_n_3_years_ago.weekday() + 1) + timedelta(weeks=1)
    
    vaccins = F_Vaccin.objects.filter(date_fk=sunday_of_next_week, local_fk__code_region='84',nb_doses__gt=0,local_fk__libelle_depart='Puy-de-Dôme')
    vaccins_paginator = Paginator(vaccins, 10)
    total_doses = vaccins.aggregate(Sum('nb_doses'))['nb_doses__sum'] or 0
    

    context = {
        'vaccins_page': vaccins_paginator,
        'total_doses': total_doses,
    }
    
    return render(request, 'index.html', context=context)
