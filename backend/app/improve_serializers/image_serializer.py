from rest_framework import serializers
from ..improve_models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'uploaded_by', 'image_file', 'uploaded_at']