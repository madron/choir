from time import time
from django.contrib.comments.models import Comment
from django.core import mail
from django.test import TestCase
from django.test.utils import override_settings
from fluent_comments.forms import CommentForm
from choir.recording.models import RecordingSong

__all__ = [
    'MailNotificationTest',
]

MANAGERS = [('Fred', 'fred@example.com'), ('Bob', 'bob@example.com')]


class MailNotificationTest(TestCase):
    fixtures = [
        'auth_test.json',
        'repertory_test.json',
        'recording_test.json',
    ]

    def setUp(self):
        self.client.login(username='tester', password='tester')
        mail.outbox = []
        self.data = self.get_base_data()

    def get_base_data(self):
        content_type = 'recording.recordingsong'
        object_pk = '1'
        timestamp = str(int(time()))
        recording_song = RecordingSong.objects.get(pk=1)
        form = CommentForm(recording_song)
        security_hash = form.generate_security_hash(
            content_type, object_pk, timestamp)
        return dict(
            content_type=content_type, object_pk=object_pk,
            timestamp=timestamp, comment='text', security_hash=security_hash)

    @override_settings(MANAGERS=MANAGERS)
    def test_post_comment(self):
        self.assertEqual(Comment.objects.count(), 0)
        response = self.client.post(
            '/comments/post/ajax/', self.data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertEqual(
            message.subject,
            '[example.com] New comment posted on "Everybody Hurts"')
        self.assertEqual(message.to, ['fred@example.com', 'bob@example.com'])
        self.assertEqual(message.from_email, 'webmaster@localhost')
