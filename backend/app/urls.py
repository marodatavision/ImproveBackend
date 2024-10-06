from django.urls import path, include
from rest_framework import routers
from .views import (
    CustomUserViewSet,
    ImageViewSet,
    AnalysisResultViewSet,
    ImprovementSuggestionViewSet
)
from django_rest_passwordreset.views import (
    reset_password_request_token,
    reset_password_confirm,
)


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'images', ImageViewSet, basename='image')
router.register(r'analysis-results', AnalysisResultViewSet, basename='analysisresult')
router.register(r'improvement-suggestions', ImprovementSuggestionViewSet, basename='improvementsuggestion')

urlpatterns = [
    path('', include(router.urls)),
    path('password_reset/', reset_password_request_token, name='password_reset'),
    path('password_reset_confirm/', reset_password_confirm, name='password_reset_confirm'),
]
