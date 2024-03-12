from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.contrib.auth.models import User
from django.conf import settings
from api.views import TypeAPIView



api_key = getattr(settings, 'API_KEY', '')
factory = APIRequestFactory()
user = User.objects.get(username='admin')
req = factory.get('Types/',headers={'Authorization': 'Token '+ api_key})

view = TypeAPIView.as_view()
type_vac = "Janssen"
wrong_type_vac = "Astra Zeneca"

launchREQ_ID = view(req,type_vac=type_vac)
launchREQ_ID.render()
launchREQ = view(req)
launchREQ.render()
launchREQ_IDW = view(req,type_vac=wrong_type_vac)
launchREQ_IDW.render()

class TestType(TestCase):
    """
    Classe de tests pour les vues des types de vaccins.
    """
    def setUp(self):
        pass

    def test_get_all(self):
        try:
            self.assertEqual(launchREQ.status_code, status.HTTP_200_OK)
        except AssertionError as e:
            self.fail(f"get_id failed: {e}")
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def test_get_all_data(self):
        try:
            self.assertEqual(launchREQ.status_code, status.HTTP_200_OK)
            self.assertEqual(launchREQ.data['data'],[
                {
                    "type_vac": "AstraZeneca"
                },
                {
                    "type_vac": "Janssen"
                },
                {
                    "type_vac": "Moderna"
                },
                {
                    "type_vac": "Pfizer"
                },
                {
                    "type_vac": "Pfizer Pédiatrique"
                }
            ])
        except AssertionError as e:
            self.fail(f"get_id failed: {e}")
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def test_get_id(self):
        try:
            self.assertEqual(launchREQ_ID.status_code, status.HTTP_200_OK)
        except AssertionError as e:
            self.fail(f"get_id failed: {e}")
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def test_get_wrong_id(self):
        try:
            self.assertEqual(launchREQ_IDW.status_code, status.HTTP_404_NOT_FOUND)
        except AssertionError as e:
            self.fail(f"get_id failed: {e}")
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def test_get_lignes(self):
        try:
            self.assertEqual(launchREQ.status_code, status.HTTP_200_OK)
            self.assertEqual(launchREQ.data['nombre_de_lignes'], 5)
        except AssertionError as e:
            self.fail(f"get_id failed: {e}")
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")
