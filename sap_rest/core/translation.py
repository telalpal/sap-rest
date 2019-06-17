from modeltranslation.translator import register, TranslationOptions
from sap_rest.core.models import Question, Folder


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = Question.FIELDS_TO_TRANSLATE


@register(Folder)
class FolderTranslationOptions(TranslationOptions):
    fields = Folder.FIELDS_TO_TRANSLATE
