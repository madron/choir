from django.contrib import admin
from . import models
from . import forms


class EventSongInline(admin.TabularInline):
    model = models.EventSong
    autocomplete_fields = ['song']
    extra = 1


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = ('date', 'slug', 'type', 'name', 'location')
    form = forms.EventForm
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
