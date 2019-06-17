from django.db import models
from django.utils.translation import ugettext_lazy as _
from sap_rest.core.constants import QUESTION_TYPE_CHOICES
from sap_rest.core.models.base import SapRestBaseModel
from sap_rest.core.models.mixins import GetTranslationsMixin


class Question(GetTranslationsMixin, SapRestBaseModel):
    FIELDS_TO_TRANSLATE = ('text',)

    template = models.ForeignKey('Template', on_delete=models.CASCADE)
    text = models.TextField(_('Text of Question'), )
    qtype = models.IntegerField(_('Type of Question'), choices=QUESTION_TYPE_CHOICES, default=1)

    def __str__(self):
        return f'Question: {self.id}|{self.text[:25]}'
