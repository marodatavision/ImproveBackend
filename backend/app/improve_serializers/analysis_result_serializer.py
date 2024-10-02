from rest_framework import serializers
from ..improve_models import AnalysisResult


class AnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisResult
        fields = ['id', 'image', 'environment', 'objects_detected', 'analyzed_at']