from datetime import datetime, timezone
from django.test import TestCase
from choir.events import models
from . import factories


class EventModelTest(TestCase):
    def test_str(self):
        event = models.Event(slug='2025-10-15')
        self.assertEqual(str(event), '2025-10-15')

    def test_slug_empty_date(self):
        event = factories.EventFactory(id=1)
        self.assertEqual(event.slug, '1')

    def test_slug_date_ok(self):
        event = factories.EventFactory(id=1, date=datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event.slug, '2025-10-15')

    def test_slug_same_date_2(self):
        event = factories.EventFactory(id=10, date=datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event.slug, '2025-10-15')
        event = factories.EventFactory(id=20, date=datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event.slug, '2025-10-15-2')

    def test_slug_same_date_3(self):
        event = factories.EventFactory(id=10, date=datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event.slug, '2025-10-15')
        event = factories.EventFactory(id=11, date=datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event.slug, '2025-10-15-2')
        event = factories.EventFactory(id=20, date=datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event.slug, '2025-10-15-3')

    def test_slug_update(self):
        event = factories.EventFactory(id=10, date=datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event.slug, '2025-10-15')
        event = factories.EventFactory(id=11, date=datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event.slug, '2025-10-15-2')
        event = factories.EventFactory(id=20, date=datetime(2025, 10, 20, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event.slug, '2025-10-20')
        event.date = datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc)
        event.save()
        self.assertEqual(event.slug, '2025-10-15-3')

    def test_slug_delete_update(self):
        event_1 = factories.EventFactory(date=datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event_1.slug, '2025-10-15')
        event_2 = factories.EventFactory(date=datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event_2.slug, '2025-10-15-2')
        event_3 = factories.EventFactory(date=datetime(2025, 10, 15, 12, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(event_3.slug, '2025-10-15-3')
        # First event is deleted
        event_1.delete()
        event_3.save()
        self.assertEqual(event_3.slug, '2025-10-15-3')
