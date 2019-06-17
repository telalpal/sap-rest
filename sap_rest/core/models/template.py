from django.db import models
from django.utils.translation import ugettext_lazy as _
from sap_rest.core.models.base import SapRestBaseModel


class Template(SapRestBaseModel):
    folder = models.ForeignKey(to='Folder', on_delete=models.CASCADE)
    title = models.CharField(_('Title of Template'), max_length=255)

    def __str__(self):
        return f'Template: {self.id}|{self.title}'
