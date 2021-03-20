from django.test import TestCase
from choir.member.models import Member

__all__ = [
    'MemberModelTest',
]


class MemberModelTest(TestCase):
    def test_unicode_nickname(self):
        member = Member(name='Frederick', surname='Flinstones',
            nickname='Fred')
        self.assertEqual(unicode(member), 'Fred (Frederick Flinstones)')

    def test_unicode_no_nickname(self):
        member = Member(name='Frederick', surname='Flinstones')
        self.assertEqual(unicode(member), 'Frederick Flinstones')

    def test_admin_url(self):
        member = Member(id=1, name='Frederick', surname='Flinstones')
        self.assertEqual(member.get_admin_url(), '/admin/member/member/1/')
