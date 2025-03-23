from django.test import TestCase

from guests.factories import GuestFactory
from guests.serializers import GuestSerializer


class GuestSerializerTestCase(TestCase):
    def setUp(self):
        self.guest = GuestFactory()

    def test_serialize(self):
        serializer = GuestSerializer(self.guest)
        self.assertEqual(serializer.data.get('id'), str(self.guest.id))
        for field in  (
            'first_name',
            'last_name',
            'email',
            'phone',
            'attending',
            'is_vegan',
            'is_vegetarian',
            'common_allergies',
            'other_allergies',
        ):
            self.assertIn(field, serializer.data)
            self.assertEqual(serializer.data[field], getattr(self.guest, field))

    def test_update(self):
        serializer = GuestSerializer(self.guest, data={
            'attending': 1,
            'is_vegan': True,
            'is_vegetarian': False,
            'common_allergies': ['nuts'],
        }, partial=True)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        serializer.save()
        self.guest.refresh_from_db()
        for field in  (
            'attending',
            'is_vegan',
            'is_vegetarian',
            'common_allergies',
        ):
            self.assertEqual(getattr(self.guest, field), serializer.validated_data[field])