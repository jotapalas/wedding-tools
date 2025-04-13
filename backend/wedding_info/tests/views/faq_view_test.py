from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from wedding_info.factories import FAQFactory
from wedding_info.models import FAQ


class FAQViewTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        for i in range(5):
            FAQFactory()
        self.url = reverse('wedding-info-faqs')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 5, response.data)
        data_dict = { d.get('id'): d for d in response.data }
        for faq in FAQ.objects.all():
            returned_data = data_dict.get(str(faq.id), None)
            self.assertIsNotNone(returned_data, f'{faq.id} not found in {response.data}')
            self.assertEqual(returned_data.get('answer'), faq.answer, response.data)
            self.assertEqual(returned_data.get('question'), faq.question, response.data)