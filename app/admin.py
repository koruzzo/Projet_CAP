from django.contrib import admin
from app.models import Vaccination
from rest_framework.authtoken.admin import TokenAdmin
from api.models import D_Date, D_Localisation, D_Type, F_Vaccin


admin.site.register(Vaccination)
admin.site.register(D_Date)
admin.site.register(D_Localisation)
admin.site.register(D_Type)
admin.site.register(F_Vaccin)
