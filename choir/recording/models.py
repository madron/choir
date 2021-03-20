from django.core.urlresolvers import reverse
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from choir.repertory.models import SONG_FILE_TYPES, Song

REC_TYPES = ('soprano', 'contralto', 'tenore', 'basso')
RECORDING_TYPES = [('music', _('Music')), ('soloist', _('Soloist'))]
RECORDING_TYPES += [x for x in SONG_FILE_TYPES if x[0] in REC_TYPES]
STATUS_CHOICES = (
    ('ok', _('Ok')),
    ('no', _('No')),
    ('review', _('Review')),
    ('partial', _('Partial')),
    ('fix', _('Fix')),
    ('improve', _('Improve')),
)
SONG_PART = dict(
    music=0,
    soloist=1,
    soprano=10,
    contralto=20,
    tenore=30,
    basso=40,
)


class RecordingSong(models.Model):
    importance = models.PositiveIntegerField(
        _('importance'), null=True, blank=True)
    song = models.OneToOneField(Song, verbose_name=_('song'))
    completed = models.BooleanField(_('completed'), default=False)

    class Meta:
        verbose_name = _('recording song')
        verbose_name_plural = _('recording songs')
        ordering = ('completed', '-importance', 'song__name')

    def __unicode__(self):
        return unicode(self.song)

    def save(self):
        super(RecordingSong, self).save()
        for t, order in SONG_PART.iteritems():
            part, created = RecordingSongPart.objects.get_or_create(
                recording_song=self, type=t)
            if not part.order == order:
                part.order = order
                part.save()

    def get_absolute_url(self):
        return reverse(
            'admin:recording_recordingsong_change', args=(self.pk,))

    def get_link(self):
        title = _('Recording')
        label = '<i class="icon-headphones"></i>'
        return mark_safe('<a href="%s" title="%s">%s</a>' % (
            self.get_absolute_url(), title, label))
    get_link.allow_tags = True

    def get_status_display(self, type):
        parts = self.recordingsongpart_set.filter(type=type)
        label = ''
        html_class = 'recording-song-part-status'
        title = ''
        if parts:
            part = parts[0]
            label = part.get_status_display()
            if part.status:
                html_class = '%s-%s' % (html_class, part.status)
            if part.note:
                title = u' title="%s"' % part.note
            else:
                title = ''
        return u'<span class="%s"%s>%s</span>' % (html_class, title, label)

    def music_status(self):
        return self.get_status_display('music')
    music_status.short_description = _('music')
    music_status.allow_tags = True

    def soloist_status(self):
        return self.get_status_display('soloist')
    soloist_status.short_description = _('soloist')
    soloist_status.allow_tags = True

    def soprano_status(self):
        return self.get_status_display('soprano')
    soprano_status.short_description = _('soprano')
    soprano_status.allow_tags = True

    def contralto_status(self):
        return self.get_status_display('contralto')
    contralto_status.short_description = _('contralto')
    contralto_status.allow_tags = True

    def tenore_status(self):
        return self.get_status_display('tenore')
    tenore_status.short_description = _('tenore')
    tenore_status.allow_tags = True

    def basso_status(self):
        return self.get_status_display('basso')
    basso_status.short_description = _('basso')
    basso_status.allow_tags = True



class RecordingSongPart(models.Model):
    recording_song = models.ForeignKey(RecordingSong)
    order = models.PositiveIntegerField(_('order'), null=True, blank=True,
        editable=False)
    type = models.CharField(_('type'), max_length=50, choices=RECORDING_TYPES)
    status = models.CharField(_('status'), max_length=50, blank=True,
        choices=STATUS_CHOICES)
    note = models.CharField(_('note'), max_length=200, blank=True)

    class Meta:
        verbose_name = _('recording song part')
        verbose_name_plural = _('recording song parts')
        ordering = ('order',)

    def __unicode__(self):
        return unicode(self.type)
