from django.conf.urls.defaults import patterns, url
from choir.repertory.views import SongListView, SongDetailView

urlpatterns = patterns("",
    url(r"^$", SongListView.as_view(), name="song_list"),
    url(r'^(?P<slug>[-\w]+)/$', SongDetailView.as_view(), name='song_detail'),
)
