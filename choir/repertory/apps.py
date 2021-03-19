from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RepertoryConfig(AppConfig):
    name = 'choir.repertory'
    verbose_name = _('Repertory')
