from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from sap_rest.rest.serializers import QuestionSerializer
from sap_rest.core.models import Question


class QuestionViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Questions to be viewed.
    """
    def retrieve(self, _, pk=None):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
