from django.test import TestCase
from django.contrib.auth import authenticate
from core.exceptions import ConflictException
from users.factories import UserFactory
from users.models import User
from users.serializers.input import UserCreateSerializer


class UserCreateSerializerTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.existing_user = UserFactory(
            username='username',
            email='email@test.es'
        )
        self.valid_data = {
            'username': 'other_username',
            'email': 'other_email@test.es',
            'password': 'p4ssw0rD!'
        }

    def test_create_user(self):
        before_count = User.objects.count()
        serializer = UserCreateSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(User.objects.count(), before_count + 1)
        self.assertTrue(User.objects.filter(username=self.valid_data['username']).exists())

    def test_user_can_authenticate(self):
        serializer = UserCreateSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        
        authenticated_user = authenticate(
            username=self.valid_data['username'],
            password=self.valid_data['password']
        )
        created_user = User.objects.get(username=self.valid_data['username'])
        self.assertEqual(created_user, authenticated_user)

    def test_missing_username(self):
        self.valid_data.pop('username')
        serializer = UserCreateSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors.keys())

    def test_missing_email(self):
        self.valid_data.pop('email')
        serializer = UserCreateSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors.keys())

    def test_invalid_email(self):
        self.valid_data['email'] = 'invalid_email'
        serializer = UserCreateSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors.keys())
    
    def test_missing_password(self):
        self.valid_data.pop('password')
        serializer = UserCreateSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors.keys())

    def test_conflicting_username(self):
        self.valid_data['username'] = self.existing_user.username
        serializer = UserCreateSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        with self.assertRaises(ConflictException):
            serializer.save()

    def test_conflicting_email(self):
        self.valid_data['email'] = self.existing_user.email
        serializer = UserCreateSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        with self.assertRaises(ConflictException):
            serializer.save()