import autocomplete_light
from choir.repertory import models


class AutocompleteSong(autocomplete_light.AutocompleteModelBase):
    search_fields = ('name',)
    autocomplete_js_attributes = {'placeholder': '...'}

    def choices_for_request(self):
        period_id = self.request.GET.get('period_id', None)
        usage_id = self.request.GET.get('usage_id', None)
        choices = super(AutocompleteSong, self).choices_for_request()
        if period_id:
            choices = choices.filter(period_id=period_id)
        if usage_id:
            choices = choices.filter(usage_id=usage_id)
        return self.order_choices(choices)[0:self.limit_choices]

    def choice_label(self, choice):
        return choice.get_name_period_usage()


autocomplete_light.register(
    models.Period, search_fields=('name',),
    autocomplete_js_attributes={'placeholder': '...'})

autocomplete_light.register(
    models.Usage, search_fields=('name',),
    autocomplete_js_attributes={'placeholder': '...'})

autocomplete_light.register(models.Song, AutocompleteSong)
