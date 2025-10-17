from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


EVENT_TYPE = dict(
    rehearsal=_('Rehearsal'),
    live=_('Live'),
    other=_('Other'),
)
EVENT_TYPES = [(k, v) for (k, v) in EVENT_TYPE.items()]
DEFAULT_EVENT_TYPE = 'rehearsal'


class Event(models.Model):
    date = models.DateTimeField(_('date'), null=True, blank=True, db_index=True)
    slug = models.SlugField(_('slug'), max_length=200, unique=True, db_index=True)
    type = models.CharField(_('type'), max_length=20, choices=EVENT_TYPES, default=DEFAULT_EVENT_TYPE)
    name = models.CharField(_('name'), max_length=200, blank=True)
    location = models.CharField(_('location'), max_length=200, blank=True, default=settings.DEFAULT_EVENT_LOCATION)
    notes = models.TextField(_('notes'), blank=True)

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
        ordering = ('date',)

    def __str__(self):
        return self.slug


class EventSong(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, db_index=True)
    song = models.ForeignKey('repertory.Song', on_delete=models.SET_NULL, null=True)
    section = models.CharField(_('section'), max_length=200, blank=True)
    soloist = models.CharField(_('soloist'), max_length=200, blank=True)
    order = models.PositiveIntegerField(_('order'), null=True, blank=True, db_index=True)

    class Meta:
        verbose_name = _('event song')
        verbose_name_plural = _('event songs')
        ordering = ('order',)
        indexes = [
            models.Index(fields=['event', 'order']),
        ]

    def __str__(self):
        return self.song.name if self.song else ''
