from rest_framework import serializers
from sap_rest.core.models import Folder
from sap_rest.rest.serializers.icon import IconSerializer
from sap_rest.rest.serializers.base import ReadOnlySerializer


class FolderMetaSerializer(ReadOnlySerializer):
    questions = serializers.ListField()
    resources = serializers.PrimaryKeyRelatedField(source='resource_set', many=True, read_only=True)
    languages = serializers.DictField(source='_get_translations')

    class Meta:
        fields = ('questions', )


class FolderSerializer(serializers.ModelSerializer):
    icon = IconSerializer()
    meta = FolderMetaSerializer(source='*')

    class Meta:
        model = Folder
        fields = ('id', 'title', 'icon', 'meta')
