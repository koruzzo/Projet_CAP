"""
URL configuration for cap_vac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import VaccinAPIView, LocalisationAPIView, DateAPIView, TypeAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Vaccins/', VaccinAPIView.as_view(), name='Vaccin-list'),
    path('Vaccins/<str:id_vac>/', VaccinAPIView.as_view(), name='Vaccin-detail'),

    path('Localisations/', LocalisationAPIView.as_view(), name='Localisation-list'),
    path('Localisations/<str:id_local>/', LocalisationAPIView.as_view(), name='Localisation-detail'),

    path('Dates/', DateAPIView.as_view(), name='Date-list'),
    path('Dates/<str:date_fs>/', DateAPIView.as_view(), name='Date-detail'),

    path('Types/', TypeAPIView.as_view(), name='Type-list'),
    path('Types/<str:type_vac>/', TypeAPIView.as_view(), name='Type-detail')
]
