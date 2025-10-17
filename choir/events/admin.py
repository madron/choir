from django.contrib import admin
from django.utils.translation import gettext as _
from . import models
from .forms import EventForm
from . import forms


class EventSongInline(admin.TabularInline):
    model = models.EventSong
    form = forms.EventSongForm
    autocomplete_fields = ['song']
    extra = 1


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    form = EventForm
    list_display = ('type', 'name', 'date', 'location', 'total_songs', 'slug')
    list_filter = ['type']
    date_hierarchy = 'date'
    form = forms.EventForm
    save_as = True
    fieldsets = (
        (None, dict(
            fields=(
                ('type', 'date',),
                ('name', 'location',),
                ('notes',),
            ),
        )),
    )
    inlines = [EventSongInline]

    @admin.display(description=_('Songs'))
    def total_songs(self, obj):
        return obj.eventsong_set.count()
