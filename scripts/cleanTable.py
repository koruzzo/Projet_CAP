from api.models import F_Vaccin

def run():
    F_Vaccin.objects.all().delete()