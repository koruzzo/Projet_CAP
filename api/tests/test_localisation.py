from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from api.views import LocalisationAPIView

factory = APIRequestFactory()

view = LocalisationAPIView.as_view()
req = factory.get('Localisations/')
id_local = "84-01"
wrong_id_local = "84-011"

launchREQ_ID = view(req,id_local=id_local)
launchREQ_ID.render()
launchREQ = view(req)
launchREQ.render()
launchREQ_IDW = view(req,id_local=wrong_id_local)
launchREQ_IDW.render()

class TestLocalisation(TestCase):
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
                    "id_local": "84-01",
                    "code_region": "84",
                    "code_depart": "01",
                    "libelle_region": "ARA",
                    "libelle_depart": "Ain"
                },
                {
                    "id_local": "32-02",
                    "code_region": "32",
                    "code_depart": "02",
                    "libelle_region": "HDF",
                    "libelle_depart": "Aisne"
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
            self.assertEqual(launchREQ.data['nombre_de_lignes'], 101)
        except AssertionError as e:
            self.fail(f"get_id failed: {e}")
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")
