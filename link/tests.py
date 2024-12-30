from django.test import TestCase
from link.models import Link
from rest_framework_api_key.models import APIKey
from rest_framework.test import APIClient
from rest_framework import status


class LinkTestCase(TestCase):

    def setUp(self):
        _, self.generated_key = APIKey.objects.create_key(name="test")
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Api-Key {str(self.generated_key)}')

    def test_create_short_link(self):
        data = {
            "main_link": "https://test.com"
        }
        response = self.client.post("/link/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["main_link"], data["main_link"])

    def test_list_short_link(self):
        data_1 = {
            "main_link": "https://test1.com"
        }
        self.client.post("/link/", data=data_1)
        data_2 = {
            "main_link": "https://test2.com"
        }
        self.client.post("/link/", data=data_2)
        response = self.client.get("/link/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)


class LinkRedirectCase(TestCase):

    def setUp(self):
        _, self.generated_key = APIKey.objects.create_key(name="test")
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Api-Key {str(self.generated_key)}')
        data_1 = {
            "main_link": "https://test1.com"
        }
        self.response = self.client.post("/link/", data=data_1)

    def test_redirect_short_link(self):
        redirect_test_client = APIClient()
        redirect_response = redirect_test_client.get(
            ("/" + self.response.json()["shorted_link"]))
        self.assertEqual(redirect_response.status_code,
                         status.HTTP_301_MOVED_PERMANENTLY)
