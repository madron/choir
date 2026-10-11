from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path('', views.EventListView.as_view(), name="event_list"),
    path('<slug:slug>/', views.EventDetailView.as_view(), name="event_detail"),
    path('<slug:event_slug>/player/<slug:song_slug>/<slug:section>/', views.EventSongPlayerView.as_view(), name="player"),
]
