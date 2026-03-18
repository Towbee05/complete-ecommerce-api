from django.tests import APITestCase, APIClient
from django.urls import reverse
from faker import Faker

faker = Faker()
class TestAddProduct(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse("product:add_product")

    def add_product(self):
        payload = {
            "name" : "product name",
            "description": "some description",
            "category": 2,
            "price" : 39.99,
            "thumbnail" : "https://i.ebayimg.com/images/g/2lgAAeSwmrdprkvu/s-l960.webp"
        }

        response = self.client.post(self.url, data=payload, format='json')

        self.assertEqual(200, response.status_code)