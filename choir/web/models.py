from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template
from account.signals import user_signed_up


def user_signed_up_callback(sender, **kwargs):
    current_site = Site.objects.get_current()
    user = kwargs['user']
    url = reverse('admin:auth_user_change', args=(user.pk,))
    user.url = 'http://%s%s' % (current_site.domain, url)
    site_url = 'http://%s/' % current_site.domain
    from_email = user.email
    recipient_list = [x[1] for x in settings.MANAGERS]
    subject = '%s%s' % (settings.EMAIL_SUBJECT_PREFIX, user)
    template = get_template('account/signup_alert.txt')
    message = template.render(Context(dict(user=user, site_url=site_url)))
    send_mail(subject, message, from_email, recipient_list)


user_signed_up.connect(user_signed_up_callback)
