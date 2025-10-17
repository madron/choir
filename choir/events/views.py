from django.views.generic import DetailView
from choir.events import models
from .constants import CHOIR_SECTION


class EventDetailView(DetailView):
    model = models.Event
    slug_field = 'slug'
    context_object_name = 'event'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        event = context['event']
        context['choir_section'] = CHOIR_SECTION
        if event.type == 'rehearsal':
            context['title'] = event.get_type_display()
        else:
            context['title'] = event.name
        return context
