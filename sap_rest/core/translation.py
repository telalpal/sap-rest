from modeltranslation.translator import register, TranslationOptions
from sap_rest.core.models import Question, Folder, Resource, Template


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = Question.FIELDS_TO_TRANSLATE


@register(Folder)
class FolderTranslationOptions(TranslationOptions):
    fields = Folder.FIELDS_TO_TRANSLATE


@register(Resource)
class ResourceTranslationOptions(TranslationOptions):
    fields = Resource.FIELDS_TO_TRANSLATE


@register(Template)
class TemplateTranslationOptions(TranslationOptions):
    fields = Template.FIELDS_TO_TRANSLATE
