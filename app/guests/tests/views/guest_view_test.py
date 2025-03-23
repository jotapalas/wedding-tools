from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from guests.factories import GuestFactory
from guests.models import Guest


class GuestViewTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.guest = GuestFactory(nickname='nickname')
        self.url = reverse('guests-detail', kwargs={
            'guest_id': self.guest.id.hex
        })

    def test_update(self):
        response = self.client.patch(self.url, {
            'first_name': self.guest.first_name,
            'last_name': self.guest.last_name,
            'attending': Guest.AttendingStatusChoices.YES,
            'is_vegan': True,
            'is_vegetarian': False,
            'common_allergies': ['nuts'],
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.guest.refresh_from_db()
        self.assertEqual(self.guest.attending, Guest.AttendingStatusChoices.YES)
        self.assertTrue(self.guest.is_vegan)
        self.assertFalse(self.guest.is_vegetarian)
        self.assertEqual(self.guest.common_allergies, ['nuts'])

    def test_bad_request(self):
        response = self.client.patch(self.url, {
            'first_name': self.guest.first_name,
            'last_name': self.guest.last_name,
            'attending': 'yes',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_found(self):
        response = self.client.patch(reverse('guests-detail', kwargs={
            'guest_id': 'non-existing'
        }), {
            'first_name': self.guest.first_name,
            'last_name': self.guest.last_name,
            'attending': Guest.AttendingStatusChoices.YES,
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
