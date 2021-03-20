from datetime import date
from os.path import join, splitext
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_delete
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from django.utils.translation import ugettext as _

SONG_FILE_TYPES = [
    ('score', _('Score')),
    ('midi', _('Midi')),
    ('choir', _('Choir')),
    ('soprano', _('Soprano')),
    ('contralto', _('Contralto')),
    ('tenore', _('Tenore')),
    ('basso', _('Basso')),
]
SONG_FILE_TYPES_WEB = [x for x in SONG_FILE_TYPES if not x[0] == 'score']
EXTENSIONS = dict(
    midi='mid',
)
FILE_LABEL = dict(
    mp3='<i class="icon-user"></i>',
    mid='<i class="icon-music"></i>',
    pdf='<i class="icon-book"></i>',
)


class Period(models.Model):
    name = models.CharField(
        _('name'), max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = _('period')
        verbose_name_plural = _('periods')
        ordering = ('name',)

    def __unicode__(self):
        return unicode(self.name)


class Usage(models.Model):
    name = models.CharField(
        _('name'), max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = _('usage')
        verbose_name_plural = _('usages')
        ordering = ('name',)

    def __unicode__(self):
        return unicode(self.name)


class Song(models.Model):
    name = models.CharField(
        _('name'), max_length=200, unique=True, db_index=True)
    slug = models.SlugField(
        _('slug'), max_length=200, unique=True, db_index=True)
    number = models.CharField(
        _('number'), max_length=50, db_index=True, blank=True)
    page = models.PositiveIntegerField(
        _('page'), null=True, db_index=True, blank=True)
    score_number = models.PositiveIntegerField(
        _('score number'), null=True, db_index=True, blank=True)
    tempo = models.PositiveIntegerField(_('tempo'), null=True, blank=True)
    composer = models.CharField(_('composer'), max_length=200, blank=True)
    lyrics_writer = models.CharField(
        _('lyrics writer'), max_length=200, blank=True)
    periods = models.ManyToManyField(
        Period, null=True, blank=True, verbose_name=_('periods'))
    usages = models.ManyToManyField(
        Usage, null=True, blank=True, verbose_name=_('usages'))
    chords = models.TextField(_('chords'), blank=True)
    date_added = models.DateField(
        _('date added'), auto_now_add=True, null=True, db_index=True)
    date_changed = models.DateField(
        _('date changed'), auto_now=True, null=True, db_index=True)

    class Meta:
        verbose_name = _('song')
        verbose_name_plural = _('songs')
        ordering = ('name',)

    def __unicode__(self):
        return unicode(self.name)

    def get_name_period_usage(self):
        text = unicode(self.name)
        attributes = []
        if self.periods.all():
            attributes.append(self.get_periods_display())
        if self.usages.all():
            attributes.append(self.get_usages_display())
        if attributes:
            text = "%s (%s)" % (text, u' - '.join(attributes))
        return text

    def get_absolute_url(self):
        return reverse('repertory:song_detail', kwargs=dict(slug=self.slug))

    def get_admin_url(self):
        return reverse(
            'admin:repertory_song_change', args=(self.pk,))

    def get_type_files(self):
        type_files = []
        for code, description in SONG_FILE_TYPES_WEB:
            type_files.append(dict(
                code=code, description=description,
                files=self.songfile_set.filter(type=code)))
        return type_files

    def get_detail(self):
        if self.number and self.page:
            return '%s %s ( %s %s )' % (
                _('number').capitalize(), self.number,
                _('page').capitalize(), self.page)
        else:
            if self.number:
                return '%s %s' % (_('number').capitalize(), self.number)
            elif self.page:
                return '%s %s' % (_('page').capitalize(), self.page)
            else:
                return ''

    def get_page_display(self):
        if self.page:
            return unicode(self.page)
        return u''
    get_page_display.short_description = _('page')
    get_page_display.allow_tags = False

    def get_score_number_display(self):
        if self.score_number:
            return unicode(self.score_number)
        return u''
    get_score_number_display.short_description = _('score')
    get_score_number_display.allow_tags = False

    def get_tempo_display(self):
        if self.tempo:
            return unicode(self.tempo)
        return u''
    get_tempo_display.short_description = _('tempo')
    get_tempo_display.allow_tags = False

    def get_periods_display(self):
        return u', '.join([unicode(p) for p in self.periods.all()])
    get_periods_display.short_description = _('periods')
    get_periods_display.allow_tags = False

    def get_usages_display(self):
        return u', '.join([unicode(p) for p in self.usages.all()])
    get_usages_display.short_description = _('usages')
    get_usages_display.allow_tags = False

    def get_chords_display(self):
        return Truncator(self.chords).words(5, truncate=' ...')
    get_chords_display.short_description = _('chords')
    get_chords_display.allow_tags = False

    def get_chords_url(self):
        if not self.chords:
            return None
        return join(
            settings.MEDIA_URL, 'songfile', '%s-chords.pdf' % self.slug)

    def get_chords_link(self):
        url = self.get_chords_url()
        if not url:
            return ''
        title = '%s (%s)' % (self.name, _('chords').capitalize())
        extension = 'pdf'
        content = _('Format: %s' % extension)
        label = FILE_LABEL.get(extension)
        return mark_safe('<a href="%s" title="%s" data-content="%s">%s</a>' % (
            url, title, content, label))
    get_chords_link.allow_tags = True

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

    def is_new(self):
        if self.date_added:
            delta = date.today() - self.date_added
            return bool(delta.days < 20)
        return False


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
    song = models.ForeignKey(Song)
    file = models.FileField(
        _('file'), upload_to=get_song_file_name, max_length=200)
    type = models.CharField(_('type'), max_length=50, choices=SONG_FILE_TYPES)

    class Meta:
        verbose_name = _('song file')
        verbose_name_plural = _('song files')
        ordering = ('file',)

    def __unicode__(self):
        return unicode(self.type)

    def get_absolute_url(self):
        return join(settings.MEDIA_URL, str(self.file))

    def get_file_name(self):
        return str(self.file).split('/')[1]

    def get_extension(self):
        prefix, extension = splitext(str(self.file))
        return extension.strip('.')

    def get_link(self, label=None):
        title = '%s (%s)' % (self.song.name, self.type.capitalize())
        content = _('Format: %s' % self.get_extension())
        extension = self.get_extension()
        label = label or FILE_LABEL.get(extension, extension)
        return mark_safe('<a href="%s" title="%s" data-content="%s">%s</a>' % (
            self.get_absolute_url(), title, content, label))
    get_link.allow_tags = True


def songfile_pre_delete(sender, **kwargs):
    songfile = kwargs['instance']
    songfile.file.delete()


pre_delete.connect(songfile_pre_delete, sender=SongFile)
