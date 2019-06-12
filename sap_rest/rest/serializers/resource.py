from rest_framework import serializers
from sap_rest.core.models import Resource
from sap_rest.rest.serializers.base import ReadOnlySerializer


class ResourceMetaSerializer(ReadOnlySerializer):
    folder = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('folder', )


class ResourceSerializer(serializers.ModelSerializer):
    meta = ResourceMetaSerializer(source='*')
    languages = serializers.DictField(source='_get_translations')

    class Meta:
        model = Resource
        fields = ('id', 'meta', 'languages')
