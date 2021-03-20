from StringIO import StringIO
from django.test import TestCase
from choir.events.models import Event
from choir.events.utils import get_event_xls

__all__ = [
    'XlsTest',
]


class XlsTest(TestCase):
    fixtures = [
        'member_test.json',
        'repertory_test.json',
        'events_test.json',
    ]

    def test_get_event_xls(self):
        event = Event.objects.get(pk=1)
        xls = get_event_xls(event)
        buf = StringIO()
        xls.save(buf)
        self.assertTrue(buf.getvalue())
