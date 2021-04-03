from django.views.generic import ListView, DetailView
from choir.repertory.models import Song
from .models import PUBLIC_SONG_FILE_TYPES, PRIVATE_SONG_FILE_TYPES


class SongListView(ListView):
    model = Song

    def get_context_data(self, *args, **kwargs):
        context = super(SongListView, self).get_context_data(*args, **kwargs)
        context['public_file_types'] = PUBLIC_SONG_FILE_TYPES
        context['private_file_types'] = PRIVATE_SONG_FILE_TYPES
        return context


class SongDetailView(DetailView):
    model = Song
    slug_field = 'slug'
    context_object_name = 'song'
    slug_url_kwarg = 'slug'
