from django.db import models
from django.utils.translation import ugettext as _
from choir.repertory.models import Song, Period, Usage

EVENT_TYPES = (
    ('rehearsal', _('Rehearsal')),
    ('performance', _('Performance')),
)


class Event(models.Model):
    type = models.CharField(_('type'), max_length=50, blank=True,
        choices=EVENT_TYPES)
    date = models.DateField(_('date'), null=True, blank=True, db_index=True)
    time = models.TimeField(_('time'), null=True, blank=True)
    title = models.CharField(_('title'), max_length=200, blank=True)
    published = models.BooleanField(_('published'), default=False)
    description = models.TextField(_('description'), null=True, blank=True)
    period = models.ForeignKey(Period, null=True, blank=True,
        verbose_name=_('period'))
    songs = models.ManyToManyField(Song, null=True, blank=True,
        through="EventSong", verbose_name=_('songs'))

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
        ordering = ('-date', '-time', '-id')

    def __unicode__(self):
        return unicode(self.title)


class EventSong(models.Model):
    event = models.ForeignKey(Event, verbose_name=_('event'), db_index=True)
    order = models.PositiveIntegerField(_('order'), default=1)
    usage = models.ForeignKey(Usage, verbose_name=_('usage'), null=True,
        blank=True)
    song = models.ForeignKey(Song, verbose_name=_('song'))
    note = models.CharField(_('note'), max_length=200, blank=True)
    soloist = models.CharField(_('soloist'), max_length=200, blank=True)
    guide = models.CharField(_('guide'), max_length=200, blank=True)

    class Meta:
        verbose_name = _('event song')
        verbose_name_plural = _('event songs')
        ordering = ('-event__date', '-event__time', '-event__id', 'order')

    def __unicode__(self):
        return unicode(self.song)
