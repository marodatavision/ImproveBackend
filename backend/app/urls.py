from django.urls import path, include
from rest_framework import routers
from .views import (
    CustomUserViewSet,
    ImageViewSet,
    AnalysisResultViewSet,
    ImprovementSuggestionViewSet
)


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'images', ImageViewSet)
router.register(r'analysis-results', AnalysisResultViewSet)
router.register(r'improvement-suggestions', ImprovementSuggestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
