from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from guests.factories import GuestFactory


class GuestSearchViewTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.guest = GuestFactory(nickname='nickname')
        self.url = reverse('guests-search')

    def test_search_guest(self):
        response = self.client.get(self.url, {
            'first_name': self.guest.first_name,
            'last_name': self.guest.last_name,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], str(self.guest.id))

    def test_search_guest_first_name(self):
        response = self.client.get(self.url, {
            'first_name': self.guest.first_name
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], str(self.guest.id))

    def test_search_guest_last_name(self):
        response = self.client.get(self.url, {
            'last_name': self.guest.last_name
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], str(self.guest.id))

    def test_search_guest_nickname(self):
        response = self.client.get(self.url, {
            'first_name': self.guest.nickname
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], str(self.guest.id))

    def test_search_no_response(self):
        response = self.client.get(self.url, {
            'first_name': 'non-existing'
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_search_no_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
