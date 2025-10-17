from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('events/', include(('choir.events.urls', 'events'), namespace='events')),
    path('repertory/', include('choir.repertory.urls')),
    path('player/', include(('choir.player.urls', 'player'), namespace='player')),
    path('', RedirectView.as_view(pattern_name='song_list'), name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Debug toolbar
if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += debug_toolbar.toolbar.debug_toolbar_urls()
