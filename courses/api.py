# from .models import Integration
# from rest_framework import viewsets, permissions
# from .serializers import IntegrationSerializer

# class IntegrationViewSet(viewsets.ModelViewSet):
#     queryset = Integration.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = IntegrationSerializer



from .models import Course
from rest_framework import viewsets, permissions
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializer

