from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from sap_rest.rest.serializers import ResourceSerializer
from sap_rest.core.models import Resource


class ResourceViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Folders to be viewed.
    """
    def retrieve(self, _, pk=None):
        queryset = Resource.objects.all()
        resource = get_object_or_404(queryset, pk=pk)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data)
