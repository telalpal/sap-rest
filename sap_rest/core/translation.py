from modeltranslation.translator import register, TranslationOptions
from sap_rest.core.models import Question, Folder, Resource


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = Question.FIELDS_TO_TRANSLATE


@register(Folder)
class FolderTranslationOptions(TranslationOptions):
    fields = Folder.FIELDS_TO_TRANSLATE


@register(Resource)
class ResourceTranslationOptions(TranslationOptions):
    fields = Resource.FIELDS_TO_TRANSLATE
