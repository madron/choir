from datetime import date
from os.path import splitext
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.text import Truncator
from django.utils.translation import gettext as _

SONG_FILE_TYPES = [
    ('score', _('Score')),
    ('midi', _('Midi')),
    ('choir', _('Choir')),
    ('soprano', _('Soprano')),
    ('contralto', _('Contralto')),
    ('tenore', _('Tenore')),
    ('basso', _('Basso')),
]
EXTENSIONS = dict(
    midi='mid',
)


class Period(models.Model):
    name = models.CharField(_('name'), max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = _('period')
        verbose_name_plural = _('periods')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Usage(models.Model):
    name = models.CharField(_('name'), max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = _('usage')
        verbose_name_plural = _('usages')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(_('name'), max_length=200, unique=True, db_index=True)
    slug = models.SlugField(_('slug'), max_length=200, unique=True, db_index=True)
    number = models.CharField(_('number'), max_length=50, db_index=True, blank=True)
    page = models.PositiveIntegerField(_('page'), null=True, db_index=True, blank=True)
    score_number = models.PositiveIntegerField(_('score number'), null=True, db_index=True, blank=True)
    tempo = models.PositiveIntegerField(_('tempo'), null=True, blank=True)
    composer = models.CharField(_('composer'), max_length=200, blank=True)
    lyrics_writer = models.CharField(_('lyrics writer'), max_length=200, blank=True)
    periods = models.ManyToManyField(Period, blank=True, verbose_name=_('periods'))
    usages = models.ManyToManyField(Usage, blank=True, verbose_name=_('usages'))
    date_added = models.DateField(_('date added'), auto_now_add=True, null=True, db_index=True)
    date_changed = models.DateField(_('date changed'), auto_now=True, null=True, db_index=True)

    class Meta:
        verbose_name = _('song')
        verbose_name_plural = _('songs')
        ordering = ('name',)

    def __str__(self):
        return self.name


def get_song_file_name(instance, filename):
    song = instance.song
    prefix, extension = splitext(filename)
    extension = extension.lower().strip('.')
    extension = EXTENSIONS.get(extension, extension)
    prefix = 'songfile/%s' % song.slug
    if (instance.type == 'score' and extension == 'pdf') \
            or (instance.type == 'midi' and extension == 'mid') \
            or (instance.type == 'choir' and extension == 'mp3'):
        # kyrie-eleison.midi
        return '%s.%s' % (prefix, extension)
    # kyrie-eleison-soprano.mp3
    return '%s-%s.%s' % (prefix, instance.get_type_display().lower(), extension)


class SongFile(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
    file = models.FileField(_('file'), upload_to=get_song_file_name, max_length=200)
    type = models.CharField(_('type'), max_length=50, choices=SONG_FILE_TYPES)

    class Meta:
        verbose_name = _('song file')
        verbose_name_plural = _('song files')
        ordering = ('file',)

    def __str__(self):
        return self.type


@receiver(pre_delete, sender=SongFile)
def delete_songfile(sender, **kwargs):
    songfile = kwargs['instance']
    songfile.file.delete()
