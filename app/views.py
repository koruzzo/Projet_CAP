from django.shortcuts import render
from api.models import F_Vaccin
from django.core.paginator import Paginator
from datetime import date, timedelta
from django.db.models import Sum

def index(request):

    date_n_3_years_ago = date.today() - timedelta(weeks=3*52)

    sunday_of_next_week = date_n_3_years_ago - timedelta(days=date_n_3_years_ago.weekday() + 1) + timedelta(weeks=1)
    
    vaccins = F_Vaccin.objects.filter(date_fk=sunday_of_next_week, local_fk__code_region='84',nb_doses__gt=0)
    vaccins_paginator = Paginator(vaccins, 10)
    total_doses = vaccins.aggregate(Sum('nb_doses'))['nb_doses__sum'] or 0
    

    context = {
        'vaccins_page': vaccins_paginator,
        'total_doses': total_doses,
    }
    
    return render(request, 'index.html', context=context)
