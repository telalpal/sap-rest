from django.db import models
from django.utils.translation import ugettext_lazy as _
from typing import List
from sap_rest.core.models.base import SapRestBaseModel
from sap_rest.core.models.question import Question
from sap_rest.core.models.mixins import GetTranslationsMixin


class Folder(GetTranslationsMixin, SapRestBaseModel):
    FIELDS_TO_TRANSLATE = ('title', )

    icon = models.ForeignKey(to='Icon', on_delete=models.CASCADE,)
    title = models.CharField(_('Title of Folder'), max_length=255)

    def __str__(self):
        return f'Folder: {self.id}|{self.title}'

    def questions(self) -> List[int]:
        """
        collect and return all related questions
        """
        return (
            Question.objects.select_related('template__folder')
            .filter(template__folder_id=self.id)
            .values_list('id', flat=True)
        )
