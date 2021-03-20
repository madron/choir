from django.contrib import admin
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib import messages
from choir.repertory import forms
from choir.repertory import models
from choir.repertory.utils import generate_chords_file


class PeriodAdmin(admin.ModelAdmin):
    pass


class UsageAdmin(admin.ModelAdmin):
    pass


class SongFileInline(admin.TabularInline):
    model = models.SongFile


class SongAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'number', 'get_page_display', 'get_score_number_display',
        'get_tempo_display', 'get_periods_display', 'get_usages_display',
        'get_chords_display', 'composer', 'lyrics_writer', 'date_added')
    list_filter = ('periods', 'usages')
    prepopulated_fields = dict(slug=('name',))
    form = forms.SongForm
    fieldsets = (
        (None, dict(
            fields=(
                ('name', 'slug'),
                ('number', 'page', 'score_number'),
                ('tempo', 'composer', 'lyrics_writer'),
                'periods',
                'usages',
            ),
        )),
        (_('Chords'), dict(
            classes=('collapse',),
            fields=('chords',),
        )),
    )
    inlines = [SongFileInline]

    def save_model(self, request, obj, *args):
        result = super(SongAdmin, self).save_model(request, obj, *args)
        song = obj
        if settings.CHORDS_ENABLED and song.chords:
            stderr = generate_chords_file(song)
            if stderr:
                messages.warning(request, stderr)
            else:
                messages.success(request, 'Chords pdf successfully saved.')
        return result
