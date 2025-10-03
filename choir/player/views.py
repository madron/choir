from django.views.generic import TemplateView


class PlayerView(TemplateView):
    template_name = 'player/player.html'

    def get_context_data(self, file_slug, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['file_slug'] = file_slug
        return context
