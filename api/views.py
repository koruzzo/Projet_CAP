from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from api.models import D_Date, D_Type, D_Localisation, F_Vaccin
from .serializers import FVaccinSerializer, DDateSerializer, DLocalisationSerializer, DTypeSerializer

class VaccinAPIView(APIView):
    """
    API View pour récupérer les données sur les vaccins.
    """
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id_vac=None):
        """
        Récupère les données sur les vaccins.

        Args:
            request: La requête HTTP reçue par la vue.
            id_vac (str): L'ID du vaccin à récupérer.

        Returns:
            Response: La réponse HTTP contenant les données sur les vaccins.
        """
        if id_vac:
            try:
                vaccin = F_Vaccin.objects.get(id_vac=id_vac)
                serializer = FVaccinSerializer(vaccin)
                return Response(serializer.data)
            except F_Vaccin.DoesNotExist:
                return Response({"error": "Aucun Vaccin ne correspond à cette ID"}, status=status.HTTP_404_NOT_FOUND)
        else:
            paginator = PageNumberPagination()
            paginator.page_size = 2
            vaccins = F_Vaccin.objects.all()
            nombre_de_lignes = vaccins.count()
            vaccins = paginator.paginate_queryset(vaccins, request)
            serializer = FVaccinSerializer(vaccins, many=True)
            result = {
                'nombre_de_lignes': nombre_de_lignes,
                'data': serializer.data,
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link()
            }
            return Response(result, status=status.HTTP_200_OK)

class LocalisationAPIView(APIView):
    """
    API View pour récupérer les données sur les localisations.
    """
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id_local=None):
        """
        Récupère les données sur les localisations.

        Args:
            request: La requête HTTP reçue par la vue.
            id_local (str): L'ID de la localisation à récupérer.

        Returns:
            Response: La réponse HTTP contenant les données sur les localisations.
        """
        if id_local:
            try:
                locali = D_Localisation.objects.get(id_local=id_local)
                serializer = DLocalisationSerializer(locali)
                return Response(serializer.data)
            except D_Localisation.DoesNotExist:
                return Response({"error": "Aucune localisation ne correspond à cette ID"}, status=status.HTTP_404_NOT_FOUND)
        else:
            paginator = PageNumberPagination()
            paginator.page_size = 2
            localis = D_Localisation.objects.all()
            nombre_de_lignes = localis.count()
            localis = paginator.paginate_queryset(localis, request)
            serializer = DLocalisationSerializer(localis, many=True)
            result = {
                'nombre_de_lignes': nombre_de_lignes,
                'data': serializer.data,
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link()
            }
            return Response(result, status=status.HTTP_200_OK)
      
class DateAPIView(APIView):
    """
    API View pour récupérer les données sur les dates.
    """
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, date_fs=None):
        """
        Récupère les données sur les dates.

        Args:
            request: La requête HTTP reçue par la vue.
            date_fs (str): La date à récupérer.

        Returns:
            Response: La réponse HTTP contenant les données sur les dates.
        """
        if date_fs:
            try:
                date = D_Date.objects.get(date_fs=date_fs)
                serializer = DDateSerializer(date)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except D_Date.DoesNotExist:
                return Response({"error": "Aucune date ne correspond à cette ID"}, status=status.HTTP_404_NOT_FOUND)
        else:
            paginator = PageNumberPagination()
            paginator.page_size = 10
            dates = D_Date.objects.all()
            nombre_de_lignes = dates.count()
            dates = paginator.paginate_queryset(dates, request)
            serializer = DDateSerializer(dates, many=True)
            result = {
                'nombre_de_lignes': nombre_de_lignes,
                'data': serializer.data,
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link()
            }
            return Response(result, status=status.HTTP_200_OK)

class TypeAPIView(APIView):
    """
    API View pour récupérer les données sur les types de vaccins.
    """
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, type_vac=None):
        """
        Récupère les données sur les types de vaccins.

        Args:
            request: La requête HTTP reçue par la vue.
            type_vac (str): Le type de vaccin à récupérer.

        Returns:
            Response: La réponse HTTP contenant les données sur les types de vaccins.
        """
        if type_vac:
            try:
                typeVa = D_Type.objects.get(type_vac=type_vac)
                serializer = DTypeSerializer(typeVa)
                return Response(serializer.data)
            except D_Type.DoesNotExist:
                return Response({"error": "Aucune date ne correspond à cette ID"}, status=status.HTTP_404_NOT_FOUND)
        else:
            paginator = PageNumberPagination()
            paginator.page_size = 10
            typeVas = D_Type.objects.all()
            nombre_de_lignes = typeVas.count()
            typeVas = paginator.paginate_queryset(typeVas, request)
            serializer = DTypeSerializer(typeVas, many=True)
            result = {
                'nombre_de_lignes': nombre_de_lignes,
                'data': serializer.data,
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link()
            }
            return Response(result, status=status.HTTP_200_OK)