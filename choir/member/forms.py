from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from choir.member import models


class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        widgets = dict(
            surname=forms.TextInput(attrs=dict(size=20)),
            name=forms.TextInput(attrs=dict(size=20)),
            phone_number=forms.TextInput(attrs=dict(size=15)),
            mobile_number=forms.TextInput(attrs=dict(size=15)),
            nickname=forms.TextInput(attrs=dict(size=10)),
            address=forms.TextInput(attrs=dict(size=30)),
            city=forms.TextInput(attrs=dict(size=30)),
            province=forms.TextInput(attrs=dict(size=2)),
            zip_code=forms.TextInput(attrs=dict(size=5)),
        )

    def clean_surname(self):
        value = self.cleaned_data['surname']
        user = self.cleaned_data.get('user', None)
        if user and not value:
            value = user.last_name
        if not value:
            raise ValidationError(_(u'This field is required.'))
        return value

    def clean_name(self):
        value = self.cleaned_data['name']
        user = self.cleaned_data.get('user', None)
        if user and not value:
            value = user.first_name
        return value

    def clean_email(self):
        value = self.cleaned_data['email']
        user = self.cleaned_data.get('user', None)
        if user and not value:
            value = user.email
        return value


class MassMailForm(forms.Form):
    roles = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(MassMailForm, self).__init__(*args, **kwargs)
        choices = [(x.id, x.name) for x in models.Role.objects.all()]
        choices.insert(0, (0, 'Tutti'))
        self.fields['roles'].choices = choices


class MassMailPreviewForm(forms.Form):
    pass
