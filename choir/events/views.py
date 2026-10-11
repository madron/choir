from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView, ListView
from choir.events import models
from choir.repertory.models import CHOIR_SECTIONS, CHOIR_SECTION_CHOICES
from choir.repertory.constants import SONG_FILE_TYPE


class EventListView(ListView):
    model = models.Event

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(date__gte=timezone.now().date()).order_by('date')


class EventDetailView(DetailView):
    model = models.Event
    slug_field = 'slug'
    context_object_name = 'event'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        event = context['event']
        context['base_url'] = settings.BASE_URL
        context['choir_section_choices'] = CHOIR_SECTION_CHOICES
        if event.type == 'rehearsal':
            context['title'] = event.get_type_display()
        else:
            context['title'] = event.name
        songs = []
        for eventsong in event.eventsong_set.all():
            song = dict(
                eventsong=eventsong,
                name=eventsong.song.name,
                slug=eventsong.song.slug,
                page=eventsong.song.page or '',
                number=eventsong.song.number,
                score_number=eventsong.song.score_number or '',
                score_file=eventsong.song.get_score_file,
                choir_player_url=eventsong.get_player_urls(['choir'])[0],
                choir_section_player_urls=eventsong.get_player_urls(CHOIR_SECTIONS),
            )
            songs.append(song)
        context['songs'] = songs
        return context


class EventSongPlayerView(DetailView):
    model = models.EventSong
    template_name = 'events/eventsong_player.html'

    def get_object(self, queryset=None):
        event_slug = self.kwargs['event_slug']
        song_slug = self.kwargs['song_slug']

        if queryset is None:
            queryset = self.get_queryset()
        queryset = queryset.filter(event__slug=event_slug, song__slug=song_slug)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        return obj

    def get_context_data(self, *args, **kwargs):
        from choir.repertory.models import SongFile
        context = super().get_context_data(*args, **kwargs)
        section = self.kwargs['section']
        event_song = context['object']
        song_file = get_object_or_404(SongFile, song=event_song.song, type=section)
        context['section_name'] = SONG_FILE_TYPE[section]
        context['event'] = event_song.event
        context['song_file'] = song_file
        return context
