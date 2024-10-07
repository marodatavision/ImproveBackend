from rest_framework import viewsets, permissions
from ..improve_models import Image
from ..improve_serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from ..openai import analyze_image_with_openai, process_and_store_analysis_result


class ImageViewSet(viewsets.ModelViewSet):
    #queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Image.objects.filter(uploaded_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

    def perform_create(self, serializer):
        image = serializer.save(uploaded_by=self.request.user)

        # Bildanalyse nach dem Upload
        analysis_result = analyze_image_with_openai(image.image_file.path, self.request.user)
        
        # Speichere die Analyseergebnisse
        process_and_store_analysis_result(image, self.request.user, analysis_result)

        return Response({'message': 'Image uploaded and analyzed successfully.'}, status=status.HTTP_201_CREATED)