from django.test import TestCase
from rest_framework.serializers import ValidationError

from guests.serializers import GuestSearchSerializer
from guests.factories import GuestFactory


class GuestSearchSerializerTestCase(TestCase):
    def setUp(self):
        self.guest = GuestFactory(nickname='nickname')

    def test_search(self):
        serializer = GuestSearchSerializer(data={
            'first_name': self.guest.first_name,
            'last_name': self.guest.last_name,
            'nickname': self.guest.nickname,
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertEqual(list(serializer.search()), [self.guest])
    
    def test_search_with_first_name(self):
        serializer = GuestSearchSerializer(data={
            'first_name': self.guest.first_name,
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertEqual(list(serializer.search()), [self.guest])

    def test_search_with_last_name(self):
        serializer = GuestSearchSerializer(data={
            'last_name': self.guest.last_name,
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertEqual(list(serializer.search()), [self.guest])

    def test_search_with_nickname(self):
        serializer = GuestSearchSerializer(data={
            'nickname': self.guest.nickname,
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertEqual(list(serializer.search()), [self.guest])

    def test_search_with_no_data(self):
        serializer = GuestSearchSerializer(data={})
        self.assertFalse(serializer.is_valid(), serializer.errors)

    def test_search_with_no_data_raise_exception(self):
        serializer = GuestSearchSerializer(data={})
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_with_incomplete_first_name(self):
        serializer = GuestSearchSerializer(data={
            'first_name': self.guest.first_name[:3],
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertEqual(list(serializer.search()), [self.guest])

    def test_with_incomplete_last_name(self):
        serializer = GuestSearchSerializer(data={
            'last_name': self.guest.last_name[:3],
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertEqual(list(serializer.search()), [self.guest])

    def test_with_incomplete_nickname(self):
        serializer = GuestSearchSerializer(data={
            'nickname': self.guest.nickname[:3],
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertEqual(list(serializer.search()), [self.guest])
