from django.test import TestCase
from django.urls import reverse
from authentication.tests.factories import UserFactory
from . import factories


class SongAdminTest(TestCase):
    def setUp(self):
        UserFactory(username='test')
        self.assertTrue(self.client.login(username='test', password='pass'))
        self.list = reverse('admin:repertory_song_changelist')
        self.obj = factories.SongFactory()

    def test_list(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        data = dict(q='text')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:repertory_song_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        url = reverse('admin:repertory_song_change', args=(self.obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        url = reverse('admin:repertory_song_delete', args=(self.obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
