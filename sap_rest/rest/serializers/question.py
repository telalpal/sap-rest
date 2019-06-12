from rest_framework import serializers
from sap_rest.core.models import Question
from sap_rest.rest.serializers.base import ReadOnlySerializer


class QuestionMetaSerializer(ReadOnlySerializer):
    folder = serializers.PrimaryKeyRelatedField(source='template.folder', read_only=True)

    class Meta:
        fields = ('folder', )


class QuestionSerializer(serializers.ModelSerializer):
    meta = QuestionMetaSerializer(source='*')
    languages = serializers.DictField(source='_get_translations')

    class Meta:
        model = Question
        fields = ('id', 'meta', 'languages')
