from django.contrib import admin
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib import messages
from choir.repertory import forms
from choir.repertory import models


@admin.register(models.Period)
class PeriodAdmin(admin.ModelAdmin):
    model = models.Period


@admin.register(models.Usage)
class UsageAdmin(admin.ModelAdmin):
    model = models.Usage


class SongFileInline(admin.TabularInline):
    model = models.SongFile


@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    model = models.Song
    list_display = (
        'name', 'number', 'page', 'score_number',
        'tempo', 'composer', 'lyrics_writer', 'date_added')
    list_filter = ('periods', 'usages')
    prepopulated_fields = dict(slug=('name',))
    form = forms.SongForm
    fieldsets = (
        (None, dict(
            fields=(
                ('name', 'slug'),
                ('number', 'page', 'score_number'),
                ('tempo', 'composer', 'lyrics_writer'),
                ('periods', 'usages'),
            ),
        )),
    )
    inlines = [SongFileInline]
