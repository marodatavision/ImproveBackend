from rest_framework import viewsets, permissions
from ..improve_models import CustomUser
from ..improve_serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Nur den angemeldeten Benutzer zurückgeben
        return CustomUser.objects.filter(id=self.request.user.id)