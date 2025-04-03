import uuid
from django.test import TestCase
from django.utils.crypto import get_random_string
from core.utils import is_valid_uuid


class UtilsTestCase(TestCase):
    def test_is_valid_uuid(self):
        self.assertTrue(is_valid_uuid(uuid.uuid4()))
        self.assertFalse(is_valid_uuid(get_random_string(length=16)))
