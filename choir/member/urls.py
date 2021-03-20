from django.conf.urls.defaults import patterns, url
from choir.member.forms import MassMailForm, MassMailPreviewForm
from choir.member.views import MemberListView

urlpatterns = patterns("",
    url(r'^$', MemberListView.as_view(
        [MassMailForm, MassMailPreviewForm]), name='member_list'),
)
