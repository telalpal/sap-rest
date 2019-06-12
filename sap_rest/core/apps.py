from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    name = "sap_rest.core"
    verbose_name = _("Core")

    def ready(self):
        try:
            import sap_rest.users.signals  # noqa F401
        except ImportError:
            pass
