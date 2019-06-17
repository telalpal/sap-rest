from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from sap_rest.rest.serializers import FolderSerializer, QuestionSerializer, ResourceSerializer
from sap_rest.core.models import Folder, Question, Resource


class FolderViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Folders to be viewed.
    """

    def list(self, _):
        queryset = Folder.objects.all().select_related('icon')
        serializer = FolderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, _, pk=None):
        queryset = Folder.objects.all()
        folder = get_object_or_404(queryset, pk=pk)
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def questions(self, _, pk=None):
        queryset = Folder.objects.all()
        folder = get_object_or_404(queryset, pk=pk)
        question_ids = folder.questions()
        questions_queryset = Question.objects.filter(pk__in=question_ids).select_related('template')
        serializer = QuestionSerializer(questions_queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def resources(self, _, pk=None):
        queryset = Folder.objects.all()
        folder = get_object_or_404(queryset, pk=pk)
        resources_queryset = Resource.objects.filter(folder=folder)
        serializer = ResourceSerializer(resources_queryset, many=True)
        return Response(serializer.data)
