from sap_rest.core.models import Icon
from rest_framework import serializers


class IconSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Icon
        fields = ('id', 'name', )
