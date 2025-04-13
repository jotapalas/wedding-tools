from django.urls import reverse
from factory.faker import faker
from rest_framework import status
from rest_framework.test import APITestCase

from users.factories import UserFactory
from users.models import User


class UserCreateViewTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        fake = faker.Faker()
        self.url = reverse('users-create')
        self.username = fake.user_name()
        self.email = fake.email()
        self.password = fake.password()
        self.body = {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }


    def test_user_is_created(self):
        before_count = User.objects.count()
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), before_count + 1)

    def test_conflict_username(self):
        existing_user = UserFactory(username=self.username)
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(User.objects.filter(username=existing_user.username).count(), 1)

    def test_conflict_email(self):
        existing_user = UserFactory(email=self.email)
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(User.objects.filter(email=existing_user.email).count(), 1)

    def test_bad_request(self):
        body = {'foo': 'bar'}
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_username(self):
        del self.body['username']
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_password(self):
        del self.body['password']
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_email(self):
        del self.body['email']
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
