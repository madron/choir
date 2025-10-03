from django.test import override_settings, SimpleTestCase
from .. import backends


class S3StorageTest(SimpleTestCase):
    @override_settings(
        AWS_S3_ENDPOINT_URL='http://localhost:9000',
        AWS_QUERYSTRING_AUTH=True,
    )
    def test_url_default(self):
        backend = backends.S3Storage()
        url = backend.url('file.txt')
        self.assertTrue(url.startswith('http://localhost:9000/media/file.txt?'))

    @override_settings(
        AWS_S3_ENDPOINT_URL='http://localhost:9000',
        AWS_QUERYSTRING_AUTH=False,
    )
    def test_url_default_no_querystring_auth(self):
        backend = backends.S3Storage()
        url = backend.url('file.txt')
        self.assertEqual(url, 'http://localhost:9000/media/file.txt')

    @override_settings(
        AWS_S3_ENDPOINT_URL='http://localhost:9000',
        AWS_S3_PUBLIC_URL='https://media.example.com',
        AWS_QUERYSTRING_AUTH=True,
    )
    def test_url_public(self):
        backend = backends.S3Storage()
        url = backend.url('file.txt')
        self.assertTrue(url.startswith('https://media.example.com/media/file.txt?'))

    @override_settings(
        AWS_S3_ENDPOINT_URL='http://localhost:9000',
        AWS_S3_PUBLIC_URL='https://media.example.com',
        AWS_QUERYSTRING_AUTH=False,
    )
    def test_url_public_no_querystring_auth(self):
        backend = backends.S3Storage()
        url = backend.url('file.txt')
        self.assertEqual(url, 'https://media.example.com/media/file.txt')
