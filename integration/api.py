from .models import Integration
from rest_framework import viewsets, permissions
from .serializers import IntegrationSerializer

class IntegrationViewSet(viewsets.ModelViewSet):
    queryset = Integration.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IntegrationSerializer

# class CreateUserInMoodleViewSet(viewsets.ModelViewSet):
#     queryset = Integration.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = IntegrationSerializer