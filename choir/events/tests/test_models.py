from django.test import SimpleTestCase
from choir.events import models


class EventModelTest(SimpleTestCase):
    def test_str(self):
        event = models.Event(slug='2025-10-15')
        self.assertEqual(str(event), '2025-10-15')
