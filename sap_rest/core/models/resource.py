from django.db import models
from django.utils.translation import ugettext_lazy as _
from markdownx.models import MarkdownxField
from sap_rest.core.models.base import SapRestBaseModel
from sap_rest.core.models.mixins import GetTranslationsMixin


class Resource(GetTranslationsMixin, SapRestBaseModel):
    folder = models.ForeignKey(to='Folder', on_delete=models.CASCADE)
    title = models.CharField(_('Title of Resource'), max_length=255)
    body = MarkdownxField()

    def __str__(self):
        return f'Resource: {self.id}|{self.title}'
