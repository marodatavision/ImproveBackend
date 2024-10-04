from django.urls import path, include
from rest_framework import routers
from .views import (
    CustomUserViewSet,
    ImageViewSet,
    AnalysisResultViewSet,
    ImprovementSuggestionViewSet
)


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'images', ImageViewSet, basename='image')
router.register(r'analysis-results', AnalysisResultViewSet, basename='analysisresult')
router.register(r'improvement-suggestions', ImprovementSuggestionViewSet, basename='improvementsuggestion')

urlpatterns = [
    path('', include(router.urls)),
]
