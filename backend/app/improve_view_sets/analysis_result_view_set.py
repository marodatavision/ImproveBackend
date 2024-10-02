from rest_framework import viewsets, permissions
from ..improve_models import AnalysisResult
from ..improve_serializers import AnalysisResultSerializer


class AnalysisResultViewSet(viewsets.ModelViewSet):
    queryset = AnalysisResult.objects.all()
    serializer_class = AnalysisResultSerializer
    permission_classes = [permissions.IsAuthenticated]