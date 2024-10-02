from django.db import models


class ImprovementSuggestion(models.Model):
    analysis_result = models.OneToOneField('AnalysisResult', on_delete=models.CASCADE)
    suggestion_markdown = models.TextField()
    alternative_markdown = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Suggestion for AnalysisResult {self.analysis_result.id}"
