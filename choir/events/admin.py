from django.conf.urls.defaults import patterns, url
from django.contrib import admin
from orderable_inlines import OrderableTabularInline
from choir.events import forms
from choir.events import models
from choir.events.views import XlsEventView


class EventSongInline(OrderableTabularInline):
    model = models.EventSong
    form = forms.EventSongForm
    orderable_field = 'order'


class EventAdmin(admin.ModelAdmin):
    list_display = ('type', 'date', 'time', 'title', 'period', 'published')
    list_display_links = ('date', 'time', 'title')
    form = forms.EventForm
    fieldsets = (
        (None, dict(
            fields=(('type', 'date', 'time'),
                    ('title', 'published'),
                    'description',
                    'period',
            ),
        )),
    )
    inlines = [EventSongInline]
    save_as = True

    def get_urls(self):
        urls = patterns('',
            url(r'^(?P<pk>\d+)/xls/$',
                self.admin_site.admin_view(XlsEventView.as_view()),
                name='events_event_xls'),
        )
        return urls + super(EventAdmin, self).get_urls()
