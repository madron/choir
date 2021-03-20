from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from choir.member.models import Role, Member


class MemberListView(SessionWizardView, ListView):
    model = Member
    queryset = Member.objects.all().order_by('role', 'surname', 'name')
    paginate_by = 100

    def done(self, form_list, **kwargs):
        return HttpResponseRedirect(reverse('member:member_list'))

    def get_template_names(self, *args, **kwargs):
        templates = dict()
        templates['0'] = ['member/member_list.html']
        templates['1'] = ['member/mass_mail_preview.html']
        return templates[self.steps.current]

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, object_list=self.get_queryset())
        context.update(super(MemberListView, self).get_context_data(**kwargs))
        if self.steps.current == '1':
            roles = self.get_all_cleaned_data()['roles']
            if '0' in roles:
                context['roles'] = Role.objects.all()
                members = Member.objects.all()
            else:
                context['roles'] = Role.objects.filter(pk__in=roles)
                members = Member.objects.filter(role__in=roles)
            recipients = ['%s <%s>' % (x.get_full_name(), x.email) for x in members if x.email]
            recipients_short = ['%s' % x.email for x in members if x.email]
            context['mail_recipient'] = ', '.join(recipients)
            context['mail_recipient_short'] = '; '.join(recipients_short)
            context['members'] = members
        return context
