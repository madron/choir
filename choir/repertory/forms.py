from django import forms
from choir.repertory import models


class SongForm(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = '__all__'
