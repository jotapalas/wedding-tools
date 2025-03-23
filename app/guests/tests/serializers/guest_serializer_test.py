from django.test import TestCase

from guests.factories import GuestFactory, GuestGroupFactory
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
            'same_group_guests',
        ):
            self.assertIn(field, serializer.data)
            self.assertEqual(serializer.data[field], getattr(self.guest, field))

    def test_serialize_with_group(self):
        group = GuestGroupFactory()
        self.guest.group = group
        self.guest.save()
        expected_ids = []
        for i in range(3):
            g = GuestFactory(group=group)
            expected_ids.append(str(g.id))

        serializer = GuestSerializer(self.guest)
        same_group_guests = serializer.data.get('same_group_guests')
        self.assertEqual(len(same_group_guests), group.count - 1)
        for guest in same_group_guests:
            self.assertIn(guest['id'], expected_ids)

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