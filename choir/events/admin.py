from django.contrib import admin
from . import models


class EventSongInline(admin.TabularInline):
    model = models.EventSong
    extra = 1


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = ('date', 'slug', 'type', 'name', 'location')
    prepopulated_fields = dict(slug=('name',))
    fieldsets = (
        (None, dict(
            fields=(
                ('date', 'slug'),
                ('type', 'name'),
                ('location', 'notes'),
            ),
        )),
    )
    inlines = [EventSongInline]
