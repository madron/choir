from django.http import HttpResponse
from django.views.generic import DetailView
from choir.events.models import Event
from choir.events.utils import get_event_xls


class XlsEventView(DetailView):
    model = Event

    def get(self, request, *args, **kwargs):
        event = self.get_object()
        filename = self.get_filename(event)
        response = HttpResponse(mimetype='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        xls = get_event_xls(event)
        xls.save(response)
        return response

    def get_filename(self, event):
        name = 'event'
        if event.date:
            name = str(event.date)
        return '%s.xls' % name
