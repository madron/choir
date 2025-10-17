from django import forms
from choir.events import models


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = '__all__'
        widgets = dict(
            notes=forms.Textarea(attrs=dict(rows=6, cols=80)),
        )
