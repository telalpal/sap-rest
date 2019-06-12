from modeltranslation.translator import register, TranslationOptions
from sap_rest.core.models import Template, Question, Resource, Folder, Icon


@register(Template)
class TemplateTranslationOptions(TranslationOptions):
    fields = Template.FIELDS_TO_TRANSLATE


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = Question.FIELDS_TO_TRANSLATE


@register(Resource)
class ResourceTranslationOptions(TranslationOptions):
    fields = Resource.FIELDS_TO_TRANSLATE


@register(Folder)
class FolderTranslationOptions(TranslationOptions):
    fields = Folder.FIELDS_TO_TRANSLATE


@register(Icon)
class IconTranslationOptions(TranslationOptions):
    fields = Icon.FIELDS_TO_TRANSLATE
