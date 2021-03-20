from django.contrib import admin
from choir.member import forms


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'surname', 'name', 'nickname',
        'phone_number', 'mobile_number', 'email', 'address')
    list_display_links = ('role',)
    list_editable = ('surname', 'name', 'nickname', 'phone_number',
        'mobile_number', 'email')
    list_filter = ('role',)
    form = forms.MemberForm
    fieldsets = (
        (None, dict(
            fields=(
                'user',
                ('surname', 'name', 'nickname', 'role'),
                ('phone_number', 'mobile_number', 'email'),
                ('address', 'city', 'province', 'zip_code'),
            ),
        )),
    )

    def get_changelist_form(self, request, **kwargs):
        kwargs.setdefault('form', forms.MemberForm)
        return super(MemberAdmin, self).get_changelist_form(request, **kwargs)
