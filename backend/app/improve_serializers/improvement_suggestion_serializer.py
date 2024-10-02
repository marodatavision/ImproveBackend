from rest_framework import serializers
from ..improve_models import ImprovementSuggestion


class ImprovementSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImprovementSuggestion
        fields = ['id', 'analysis_result', 'suggestion_markdown', 'alternative_markdown', 'created_at']