from django.contrib import admin
from django.utils.translation import gettext as _
from choir.repertory import forms
from choir.repertory import models


class SongFileInline(admin.TabularInline):
    model = models.SongFile


@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    model = models.Song
    list_display = (
        'name', 'number', 'page', 'score_number',
        'tempo', 'composer', 'lyrics_writer', 'date_added')
    prepopulated_fields = dict(slug=('name',))
    form = forms.SongForm
    fieldsets = (
        (None, dict(
            fields=(
                ('name', 'slug'),
                ('number', 'page', 'score_number'),
                ('tempo', 'composer', 'lyrics_writer'),
            ),
        )),
    )
    inlines = [SongFileInline]
