from django.test import TestCase

from wedding_info.factories import FAQFactory
from wedding_info.serializers import FAQSerializer


class FAQSerializerTestCase(TestCase):
    def setUp(self):
        self.faq = FAQFactory()

    def test_serialize(self):
        serializer = FAQSerializer(self.faq)
        self.assertEqual(serializer.data.get('id'), str(self.faq.id))
        for field in  (
            'question',
            'answer',
        ):
            self.assertIn(field, serializer.data)
            self.assertEqual(serializer.data[field], getattr(self.faq, field))
