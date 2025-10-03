from django.test import TestCase
from django.urls import reverse


class PlayerViewTest(TestCase):
    def test_ok(self):
        url = reverse('player:index', args=('audio-file-slug',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'audio-file-slug.mp3')
