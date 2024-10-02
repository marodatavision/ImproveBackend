from django.db import models


class AnalysisResult(models.Model):
    image = models.OneToOneField('Image', on_delete=models.CASCADE)
    environment = models.CharField(max_length=100)
    objects_detected = models.JSONField()
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AnalysisResult for Image {self.image.id}"
