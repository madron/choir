from itertools import chain
from django import forms
from django.utils.safestring import mark_safe


class ReadonlySelect(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        value = value or ''
        choices = chain(self.choices, choices)
        choices = [c for c in choices if c[0] == value]
        label = choices[0][1]
        hidden = forms.HiddenInput().render(name, value, attrs=attrs)
        return mark_safe(u'<b>%s</b>%s' % (label, hidden))


class StatusSelect(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        attrs = attrs or dict()
        attrs['class'] = 'recording-song-part-status'
        if value:
            attrs['class'] = 'recording-song-part-status-%s' % value
        return super(StatusSelect, self).render(
            name, value, attrs=attrs, choices=choices)


class MediaPlayerWidget(forms.Widget):
    class Media:
        css = dict(all=['mediaelementjs/mediaelementplayer.min.css'])
        js = [
            'mediaelementjs/mediaelement-and-player.min.js',
            # 'recording/audio_player.js',
        ]

    def render(self, name, value, attrs=None):
        if not value:
            return ''
        html = u'<audio src="%s" type="audio/mp3" controls="controls" ' \
            'preload="none"></audio>' % value.get_absolute_url()
        return mark_safe(html)
