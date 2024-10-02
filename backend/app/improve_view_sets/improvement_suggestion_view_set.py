from rest_framework import viewsets, permissions
from ..improve_models import ImprovementSuggestion
from ..improve_serializers import ImprovementSuggestionSerializer


class ImprovementSuggestionViewSet(viewsets.ModelViewSet):
    queryset = ImprovementSuggestion.objects.all()
    serializer_class = ImprovementSuggestionSerializer
    permission_classes = [permissions.IsAuthenticated]