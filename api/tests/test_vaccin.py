from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from api.views import VaccinAPIView


factory = APIRequestFactory()

view = VaccinAPIView.as_view()
req = factory.get('Vaccins/')
id_vac = "84-01-2021-06-13-astrazeneca"
wrong_id_vac = "84-01-2021-06-13-astrazenca"

launchREQ_ID = view(req,id_vac=id_vac)
launchREQ_ID.render()
launchREQ = view(req)
launchREQ.render()
launchREQ_IDW = view(req,id_vac=wrong_id_vac)
launchREQ_IDW.render()

class TestVaccin(TestCase):
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
            expected_data = [
                {
                    "nb_ucd": 378.0,
                    "nb_doses": 3780.0,
                },
                {
                    "nb_ucd": 141.0,
                    "nb_doses": 1410.0,
                }
            ]
            actual_data = launchREQ.data['data']
            for expected, actual in zip(expected_data, actual_data):
                self.assertEqual(expected["nb_ucd"], actual["nb_ucd"])
                self.assertEqual(expected["nb_doses"], actual["nb_doses"])
        except AssertionError as e:
            self.fail(f"test_get_all_data failed: {e}")
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
            self.assertEqual(launchREQ.data['nombre_de_lignes'], 32952)
        except AssertionError as e:
            self.fail(f"get_id failed: {e}")
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")
