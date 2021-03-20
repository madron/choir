from autocomplete_light import get_widgets_dict
from django import forms
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from choir.repertory import models


class FixedModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FixedModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not isinstance(field.widget, RelatedFieldWidgetWrapper):
                continue
            if not isinstance(field.help_text, str) \
                    and not isinstance(field.help_text, unicode):
                field.help_text = ""


class SongForm(FixedModelForm):
    class Meta:
        model = models.Song
        widgets = get_widgets_dict(models.Song)
