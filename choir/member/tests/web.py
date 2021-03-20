from django.test import TestCase

__all__ = [
    'MemberAnonymousTest',
    'MemberLoggedInTest',
]


class MemberAnonymousTest(TestCase):
    fixtures = [
        'member_test.json',
    ]

    def test_member(self):
        response = self.client.get('/member/')
        self.assertContains(response, '<table class="table table-striped')
        self.assertNotContains(response, 'href="/admin/member/member/1/"')
        self.assertNotContains(response,
            'href="mailto:Frederick Flinstones <fred@example.com>"')


class MemberLoggedInTest(TestCase):
    fixtures = [
        'auth_test.json',
        'member_test.json',
    ]

    def setUp(self):
        self.client.login(username='tester', password='tester')

    def test_member(self):
        response = self.client.get('/member/')
        self.assertContains(response, '<table class="table table-striped')
        self.assertContains(response, 'href="/admin/member/member/1/"')
        self.assertContains(response,
            'href="mailto:Frederick Flinstones <fred@example.com>"')
