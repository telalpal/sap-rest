from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RestConfig(AppConfig):
    name = "sap_rest.rest"
    verbose_name = _("Core")
