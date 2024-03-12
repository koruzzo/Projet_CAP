from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.contrib.auth.models import User
from django.conf import settings
from api.views import DateAPIView

api_key = getattr(settings, 'API_KEY', '')
factory = APIRequestFactory()
user = User.objects.get(username='admin')
req = factory.get('Dates/',headers={'Authorization': 'Token '+ api_key})

view = DateAPIView.as_view()
date_fs = "2021-06-20"
wrong_date_Fs = "2021-06-21"

launchREQ_ID = view(req,date_fs=date_fs)
launchREQ_ID.render()
launchREQ = view(req)
launchREQ.render()
launchREQ_IDW = view(req,date_fs=wrong_date_Fs)
launchREQ_IDW.render()

class TestDate(TestCase):
    """
    Classe de tests pour les vues des dates.
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
                    "date_fs": "2021-06-13"
                },
                {
                    "date_fs": "2021-06-20"
                },
                {
                    "date_fs": "2021-06-27"
                },
                {
                    "date_fs": "2021-07-04"
                },
                {
                    "date_fs": "2021-07-11"
                },
                {
                    "date_fs": "2021-07-18"
                },
                {
                    "date_fs": "2021-07-25"
                },
                {
                    "date_fs": "2021-08-01"
                },
                {
                    "date_fs": "2021-08-08"
                },
                {
                    "date_fs": "2021-08-15"
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
            self.assertEqual(launchREQ.data['nombre_de_lignes'], 100)
        except AssertionError as e:
            self.fail(f"get_id failed: {e}")
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")
