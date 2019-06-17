from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from sap_rest.core.models import Icon, Folder, Resource, Question, Template


@admin.register(Resource)
class ResourceAdmin(TranslationAdmin):
    pass


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    pass


@admin.register(Folder)
class FolderAdmin(TranslationAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(TranslationAdmin):
    pass


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass
