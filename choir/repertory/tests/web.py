from django.test import TestCase

__all__ = [
    'RepertoryTest',
    'SongAdminTest',
]


class RepertoryTest(TestCase):
    fixtures = [
        'auth_test.json',
        'repertory_test.json',
    ]

    def test_anonymous(self):
        response = self.client.get('/repertory/')
        self.assertContains(response, '<table class="table table-striped')

    def test_logged_in(self):
        self.client.login(username='tester', password='tester')
        response = self.client.get('/repertory/')
        self.assertContains(response, '<table class="table table-striped')


class SongAdminTest(TestCase):
    fixtures = [
        'auth_test.json',
        'repertory_test.json',
    ]

    def setUp(self):
        self.client.login(username='tester', password='tester')

    def test_list(self):
        response = self.client.get('/admin/repertory/song/')
        self.assertContains(response, '<body class="change-list">')

    def test_detail(self):
        response = self.client.get('/admin/repertory/song/1/')
        self.assertContains(response,
            '<body class="repertory-song change-form">')
