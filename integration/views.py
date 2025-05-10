# views.py
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .deepseek import create_moodle_user
from .models import Integration  # Tu modelo de usuario local
from .serializers import IntegrationSerializer  # Tu serializer

# Create your views here.
class UserCreateView(APIView):
    def post(self, request):
        # 1. Valida los datos del usuario en tu API
        serializer = IntegrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # 2. Guarda el usuario en tu base de datos
        user = serializer.save()

 
  



























import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class MoodleCompletedCourses(APIView):
    def get(self, request, user_id):
        # Configurar parámetros para la solicitud a Moodle
        moodle_url = "http://localhost/moodle/webservice/rest/server.php"
        
        params = {
            'wstoken': "d7b823963e1a203d0010ecd8e7c73694",
            'wsfunction': 'core_enrol_get_users_courses',
            'moodlewsrestformat': "json",
            'userid': user_id,
            # 'courseid': 0  # Ajusta según la API de Moodle (ej: 0 para todos los cursos)
        }

# http://localhost/moodle/webservice/rest/server.php?
# wstoken=d7b823963e1a203d0010ecd8e7c73694&wsfunction=core_enrol_get_users_courses&
# userid=27&moodlewsrestformat=json

        try:
            # Realizar solicitud a Moodle
            response = requests.get( moodle_url, params = params)
            response.raise_for_status()  # Lanza error para respuestas no exitosas
            
            # Procesar la respuesta de Moodle
            data = response.json()
            print(data)

             # Verifica si la respuesta es una lista
            if not isinstance(data, list):
                return Response({"error": "Respuesta inválida de Moodle"}, status=500)

            # Filtra cursos completados (progreso 100%)
            completed_courses = [
                course['fullname'] 
                for course in data 
                if course.get('progress', 0) == 100
            ]

            if not completed_courses:
                return Response({"message": "El usuario no tiene cursos completados"}, status=200)

            return Response({"completed_courses": completed_courses}, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response(
                {'error': f'Error al conectar con Moodle: {str(e)}'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        

        