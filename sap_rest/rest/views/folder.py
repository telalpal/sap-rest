from rest_framework import viewsets
from rest_framework.response import Response
from sap_rest.rest.serializers import FolderSerializer
from sap_rest.core.models import Folder


class FolderViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Folders to be viewed.
    """

    def list(self, _):
        queryset = Folder.objects.all().select_related('icon')
        serializer = FolderSerializer(queryset, many=True)
        return Response(serializer.data)
