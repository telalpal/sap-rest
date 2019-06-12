from typing import Dict
from modeltranslation.fields import TranslationField
from modeltranslation.settings import AVAILABLE_LANGUAGES
from modeltranslation.utils import build_localized_fieldname


class GetTranslationsMixin:
    """
    Mixin to get all translation languages for field
    translations are come from django-modeltranslation
    """
    def _get_translations(self) -> Dict[str, Dict[str, str]]:
        result = {}
        translated_fields = getattr(self, 'FIELDS_TO_TRANSLATE', None)
        if not translated_fields:
            return result

        for lang in AVAILABLE_LANGUAGES:
            lang_translations = {}
            result[lang] = lang_translations
            for field in translated_fields:
                translated_field_name = build_localized_fieldname(field, lang)
                lang_translations[field] = getattr(self, translated_field_name, None)
        return result
