from rest_framework import serializers
from api.models import D_Date, D_Type, D_Localisation, F_Vaccin

class DTypeSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle D_Type."""
    class Meta:
        model = D_Type
        fields = '__all__'

class DDateSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle D_Date."""
    class Meta:
        model = D_Date
        fields = '__all__'

class DLocalisationSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle D_Localisation."""
    class Meta:
        model = D_Localisation
        fields = '__all__'

class FVaccinSerializer(serializers.ModelSerializer):
    """Serializer pour le modèle D_Localisation."""
    class Meta:
        model = F_Vaccin
        fields = '__all__'
