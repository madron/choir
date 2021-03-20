import autocomplete_light
from choir.member import models

autocomplete_light.register(models.Member,
    search_fields=('surname', 'name', 'nickname'),
    autocomplete_js_attributes={'placeholder': '...'})
