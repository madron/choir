from datetime import date
from os.path import splitext
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _


SONG_FILE_TYPE = dict(
    score=_('Score'),
    midi=_('Midi'),
    choir=_('Choir'),
    chords=_('Chords'),
    lyrics=_('Lyrics'),
    soprano=_('Soprano'),
    contralto=_('Contralto'),
    tenore=_('Tenore'),
    basso=_('Basso'),
)
SONG_FILE_TYPES = [(k, v) for (k, v) in SONG_FILE_TYPE.items()]
PUBLIC_SONG_FILE_TYPES = ['chords']
PUBLIC_SONG_FILE_TYPES = [(x, SONG_FILE_TYPE[x]) for x in PUBLIC_SONG_FILE_TYPES]
PRIVATE_SONG_FILE_TYPES = ['score', 'choir', 'soprano', 'contralto', 'tenore', 'basso']
PRIVATE_SONG_FILE_TYPES = [(x, SONG_FILE_TYPE[x]) for x in PRIVATE_SONG_FILE_TYPES]
EXTENSIONS = dict(
    midi='mid',
)
FILE_LABEL = dict(
    mp3='<span class="mdi mdi-music"></span>',
    mid='<span class="mdi mdi-midi"></span>',
    pdf='<span class="mdi mdi-file-pdf"></span>',
)


class Song(models.Model):
    name = models.CharField(_('name'), max_length=200, unique=True, db_index=True)
    slug = models.SlugField(_('slug'), max_length=200, unique=True, db_index=True)
    number = models.CharField(_('number'), max_length=50, db_index=True, blank=True)
    page = models.PositiveIntegerField(_('page'), null=True, db_index=True, blank=True)
    score_number = models.PositiveIntegerField(_('score number'), null=True, db_index=True, blank=True)
    tempo = models.PositiveIntegerField(_('tempo'), null=True, blank=True)
    composer = models.CharField(_('composer'), max_length=200, blank=True)
    lyrics_writer = models.CharField(_('lyrics writer'), max_length=200, blank=True)
    date_added = models.DateField(_('date added'), auto_now_add=True, null=True, db_index=True)
    date_changed = models.DateField(_('date changed'), auto_now=True, null=True, db_index=True)

    class Meta:
        verbose_name = _('song')
        verbose_name_plural = _('songs')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_chords(self):
        songfile = self.songfile_set.filter(type='chords')
        if songfile:
            return songfile[0]
        return None

    def get_chords_link(self):
        obj = self.get_chords()
        if obj:
            label = self.score_number or '<i class="icon-book"></i>'
            return obj.get_link()
            return obj.get_link(label=label)
            pass
        return ''

    def get_files(self, type_choices):
        files = dict()
        for file in self.songfile_set.all():
            files[file.type] = file
        return [files.get(x[0], None) for x in type_choices]

    def get_public_files(self):
        return self.get_files(PUBLIC_SONG_FILE_TYPES)

    def get_private_files(self):
        return self.get_files(PRIVATE_SONG_FILE_TYPES)

    def get_score(self):
        scores = self.songfile_set.filter(type='score')
        if scores:
            return scores[0]
        return None

    def get_score_display(self):
        score = self.get_score()
        if score:
            label = self.score_number or '<i class="icon-book"></i>'
            return score.get_link(label=label)
        else:
            return str(self.score_number or '')


def get_song_file_name(instance, filename):
    song = instance.song
    prefix, extension = splitext(filename)
    extension = extension.lower().strip('.')
    extension = EXTENSIONS.get(extension, extension)
    prefix = 'songfile/%s' % song.slug
    type =  SONG_FILE_TYPE[instance.type].lower()
    return '{}-{}.{}'.format(prefix, type, extension)


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

    def get_absolute_url(self):
        return self.file.url

    def get_extension(self):
        _, extension = splitext(str(self.file))
        return extension.strip('.')

    def get_link(self, label=None):
        title = '{} ({})'.format(self.song.name, SONG_FILE_TYPE[self.type])
        content = _('Format: {}'.format(self.get_extension()))
        extension = self.get_extension()
        label = label or FILE_LABEL.get(extension, extension)
        if self.type == 'score' and self.song.score_number:
            label = self.song.score_number
        return mark_safe('<a href="{}" title="{}" data-content="{}">{}</a>'.format(
            self.file.url, title, content, label))
    get_link.allow_tags = True


@receiver(pre_delete, sender=SongFile)
def delete_songfile(sender, **kwargs):
    songfile = kwargs['instance']
    songfile.file.delete()
