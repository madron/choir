from django.urls import path
from . import views

app_name = "player"


urlpatterns = [
    path("<slug:file_slug>/", views.PlayerView.as_view(), name="index"),
]
