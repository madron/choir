from django.views.generic import ListView, DetailView
from choir.repertory.models import Song, SONG_FILE_TYPES_WEB


class SongListView(ListView):
    model = Song
    paginate_by = 100

    def get_context_data(self, *args, **kwargs):
        context = super(SongListView, self).get_context_data(*args, **kwargs)
        context['file_types'] = SONG_FILE_TYPES_WEB
        return context


class SongDetailView(DetailView):
    model = Song
    slug_field = 'slug'
    context_object_name = 'song'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *args, **kwargs):
        context = super(SongDetailView, self).get_context_data(*args, **kwargs)
        user = self.request.user
        song = context['song']
        show_score = False
        show_choords = False
        if user.has_perm('repertory.change_song'):
            if song.get_score():
                show_score = True
        else:
            if song.chords:
                show_choords = True
        context['show_score'] = show_score
        context['show_choords'] = show_choords
        return context
