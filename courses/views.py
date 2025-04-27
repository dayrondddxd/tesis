from django.shortcuts import render

# Create your views here.

######### CREACION DE CURSOS ##########
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

# class CourseViewSet(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
class CourseCreateView(APIView):
    def post(self, request):
        # 1. Valida los datos del usuario en tu API
        serializer = CourseSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # 2. Guarda el usuario en tu base de datos
        course = serializer.save()

# class UserCreateView(APIView):
#     def post(self, request):
#         # 1. Valida los datos del usuario en tu API
#         serializer = IntegrationSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         # 2. Guarda el usuario en tu base de datos
#         user = serializer.save()