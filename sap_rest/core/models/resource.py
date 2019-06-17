from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from sap_rest.core.models.base import SapRestBaseModel
from sap_rest.core.models.mixins import GetTranslationsMixin


class Resource(GetTranslationsMixin, SapRestBaseModel):
    FIELDS_TO_TRANSLATE = ('title', 'body')

    folder = models.ForeignKey(to='Folder', on_delete=models.CASCADE)
    title = models.CharField(_('Title of Resource'), max_length=255)
    body = RichTextField()

    def __str__(self):
        return f'Resource: {self.id}|{self.title}'
