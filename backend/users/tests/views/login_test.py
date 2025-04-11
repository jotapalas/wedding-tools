from django.urls import reverse
from factory.faker import faker
from rest_framework import status
from rest_framework.test import APITestCase

from users.factories import UserFactory


class UserLoginTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        fake = faker.Faker()
        self.password = fake.password()
        self.wrong_password = fake.password()
        self.user = UserFactory(
            username=fake.user_name(),
            email=fake.email(),
            password=self.password
        )

    def test_login_with_username(self):
        url = reverse('users-login')
        body = {
            'username': self.user.username,
            'password': self.password
        }
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_with_email(self):
        url = reverse('users-login')
        body = {
            'username': self.user.email,
            'password': self.password
        }
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_wrong_login(self):
        url = reverse('users-login')
        body = {
            'username': self.user.username,
            'password': self.wrong_password
        }
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
