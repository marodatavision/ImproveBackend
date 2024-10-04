from rest_framework import viewsets, permissions
from ..improve_models import AnalysisResult
from ..improve_serializers import AnalysisResultSerializer


class AnalysisResultViewSet(viewsets.ModelViewSet):
    #queryset = AnalysisResult.objects.all()
    serializer_class = AnalysisResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AnalysisResult.objects.filter(image__uploaded_by=self.request.user)

    def perform_create(self, serializer):
        # Optional: Sicherstellen, dass die AnalysisResult zu einem Bild des aktuellen Nutzers gehört
        image = serializer.validated_data.get('image')
        if image.uploaded_by != self.request.user:
            raise PermissionDenied("You do not have permission to analyze this image.")
        serializer.save()