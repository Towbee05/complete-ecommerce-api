from locust import HttpUser, task, between
from faker import Faker

class LocustUser(HttpUser):
    wait_time = between(1, 5)
    @task
    def signup(self):
        print(self.key)
        fake = Faker()
        url = '/api/v1/auth/signup/'
        payload = {
            'email': fake.email(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'password': fake.password()
        }
        self.client.post(url, json=payload)