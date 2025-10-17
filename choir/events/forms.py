from django import forms
from choir.events import models


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = '__all__'
        widgets = dict(
            notes=forms.Textarea(attrs=dict(rows=1)),
        )


class EventSongForm(forms.ModelForm):
    class Meta:
        model = models.EventSong
        fields = '__all__'
        widgets = dict(
            section=forms.TextInput(attrs=dict(style='width: 10rem;')),
            soloist=forms.TextInput(attrs=dict(style='width: 8rem;')),
            order=forms.TextInput(attrs=dict(style='width: 2rem;')),
        )
