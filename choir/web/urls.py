import autocomplete_light
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import TemplateView
# from pinax.apps.account.openid_consumer import PinaxConsumer

autocomplete_light.autodiscover()
admin.autodiscover()

handler500 = "pinax.views.server_error"

urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name='homepage.html'), name="home"),
    url(r"^repertory/", include("choir.repertory.urls", namespace="repertory")),
    url(r"^member/", include("choir.member.urls", namespace="member")),
    url(r'autocomplete/', include('autocomplete_light.urls')),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    # url(r"^openid/", include(PinaxConsumer().urls)),
)

if 'fluent_comments' in settings.INSTALLED_APPS:
    urlpatterns += patterns(
        '',
        url(r'^comments/', include('fluent_comments.urls')),
    )

if settings.DEBUG:
    urlpatterns = patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ) + urlpatterns
