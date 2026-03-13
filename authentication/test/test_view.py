from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from faker import Faker
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationView(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse("authentication:auth_signup")

    def test_create_user_success(self):
        fake = Faker()
        payload = {
            'email': fake.email(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'password' : fake.password()
        }
        response = self.client.post(self.url, data=payload, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["email"], payload['email'])

    def test_create_user_email_exist(self):
        fake = Faker()
        payload = {
            'email': 'olatiseoluwatobiloba@gmail.com',
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'password': fake.password()
        }
        user = User(**payload)
        user.set_password(payload['password'])
        user.save()
        response = self.client.post(self.url, data=payload, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.data)


class UserLoginView(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse("authentication:auth_login")
        self.user = User.objects.create_user(
             email= "testemail@gmail.com",
            password="testpassword"
        )

    def test_login_success(self):
        payload = {
            "email" : "testemail@gmail.com",
            "password" : "testpassword"
        }

        response = self.client.post(self.url, data=payload, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_failure(self):
        faker = Faker()
        payload = {
            "email": faker.email(),
            "password": faker.password()
        }

        response = self.client.post(self.url, data=payload, format='json')

        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", response.data)