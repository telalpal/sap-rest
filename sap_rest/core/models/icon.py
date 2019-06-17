from django.db import models
from django.utils.translation import ugettext_lazy as _
from sap_rest.core.models.base import SapRestBaseModel


class Icon(SapRestBaseModel):
    name = models.CharField(_('Name of Icon'), max_length=255)

    def __str__(self):
        return f'Icon: {self.id}|{self.name}'
