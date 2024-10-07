from rest_framework import viewsets, permissions
from ..improve_models import Image
from ..improve_serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class ImageViewSet(viewsets.ModelViewSet):
    #queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Image.objects.filter(uploaded_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)