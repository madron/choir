from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _


class Role(models.Model):
    name = models.CharField(_('name'), max_length=200, unique=True)
    order = models.PositiveIntegerField(_('order'), null=True, blank=True)

    class Meta:
        verbose_name = _('role')
        verbose_name_plural = _('roles')
        ordering = ('order', 'name',)

    def __unicode__(self):
        return unicode(self.name)

    def get_members_with_mail(self):
        return Member.objects.filter(role=self).exclude(email='')

    def get_members_without_mail(self):
        return Member.objects.filter(role=self).filter(email='')


class Member(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
        verbose_name=_('user'))
    surname = models.CharField(_('surname'), max_length=200, blank=True)
    name = models.CharField(_('name'), max_length=200, blank=True)
    nickname = models.CharField(_('nickname'), max_length=200, blank=True)
    role = models.ForeignKey(Role, null=True, blank=True,
        related_name='member_role_pk', verbose_name=_('role'))
    phone_number = models.CharField(_('phone number'), max_length=50,
        blank=True)
    mobile_number = models.CharField(_('mobile number'), max_length=50,
        blank=True)
    email = models.CharField(_('email'), max_length=200, blank=True)
    address = models.CharField(_('address'), max_length=200, blank=True)
    city = models.CharField(_('city'), max_length=200, blank=True)
    province = models.CharField(_('province'), max_length=200, blank=True)
    zip_code = models.CharField(_('zip code'), max_length=50, blank=True)

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')
        ordering = ('role', 'surname', 'name')

    def __unicode__(self):
        if self.nickname:
            return u'%s (%s)' % (self.nickname, self.get_full_name())
        return self.get_full_name()
    __unicode__.short_description = _('member')
    __unicode__.admin_order_field = 'surname'
    __unicode__.allow_tags = False

    def get_absolute_url(self):
        return reverse('member:member_list')

    def get_admin_url(self):
        return reverse('admin:member_member_change', args=[self.pk])

    def get_full_name(self):
        return u'%s %s'.strip() % (self.name, self.surname)

    def get_phone_numbers(self):
        numbers = []
        if self.phone_number:
            numbers.append(self.phone_number)
        if self.mobile_number:
            numbers.append(self.mobile_number)
        return numbers
