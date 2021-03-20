from autocomplete_light import get_widgets_dict
from django import forms
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.utils.translation import ugettext as _
from choir.recording import models
from choir.recording.widgets import ReadonlySelect, StatusSelect
from choir.recording.widgets import MediaPlayerWidget

RECORDING_SONG_PART_WIDGETS = get_widgets_dict(models.RecordingSong)
RECORDING_SONG_PART_WIDGETS['type'] = ReadonlySelect()
RECORDING_SONG_PART_WIDGETS['status'] = StatusSelect()


class FixedModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FixedModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not isinstance(field.widget, RelatedFieldWidgetWrapper):
                continue
            if not isinstance(field.help_text, str) \
                    and not isinstance(field.help_text, unicode):
                field.help_text = ""


class RecordingSongForm(FixedModelForm):
    class Meta:
        model = models.RecordingSong
        widgets = get_widgets_dict(models.RecordingSong)


class RecordingSongPartForm(FixedModelForm):
    song_file = forms.CharField(
        label=_('song file'), required=False, widget=MediaPlayerWidget())

    class Meta:
        model = models.RecordingSongPart
        widgets = RECORDING_SONG_PART_WIDGETS

    def __init__(self, *args, **kwargs):
        self.base_fields['song_file'].initial = None
        instance = kwargs.get('instance')
        if instance:
            song = instance.recording_song.song
            song_files = song.songfile_set.filter(type=instance.type)
            song_files = [f for f in song_files if f.get_extension() == 'mp3']
            if song_files:
                song_file = song_files[0]
                self.base_fields['song_file'].initial = song_file
        super(RecordingSongPartForm, self).__init__(*args, **kwargs)
