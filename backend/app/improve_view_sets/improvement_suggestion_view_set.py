from rest_framework import viewsets, permissions
from ..improve_models import ImprovementSuggestion
from ..improve_serializers import ImprovementSuggestionSerializer


class ImprovementSuggestionViewSet(viewsets.ModelViewSet):
    #queryset = ImprovementSuggestion.objects.all()
    serializer_class = ImprovementSuggestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ImprovementSuggestion.objects.filter(
            analysis_result__image__uploaded_by=self.request.user
        )

    def perform_create(self, serializer):
        analysis_result = serializer.validated_data.get('analysis_result')
        if analysis_result.image.uploaded_by != self.request.user:
            raise PermissionDenied("You do not have permission to create suggestions for this analysis.")
        serializer.save()