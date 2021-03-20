from django.test import TestCase

__all__ = [
    'EventAdminTest',
]


class EventAdminTest(TestCase):
    fixtures = [
        'auth_test.json',
        'member_test.json',
        'repertory_test.json',
        'events_test.json',
    ]

    def setUp(self):
        self.client.login(username='tester', password='tester')

    def test_list(self):
        response = self.client.get('/admin/events/event/')
        self.assertContains(response, '<body class="change-list">')

    def test_add(self):
        response = self.client.get('/admin/events/event/add/')
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get('/admin/events/event/1/')
        self.assertContains(response, '<a href="/admin/events/event/1/xls/">')

    def test_xls(self):
        response = self.client.get('/admin/events/event/1/xls/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/vnd.ms-excel')
