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
        














































# views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MoodleQuiz(APIView):
    def get(self, request, user_id, course_id):
        MOODLE_URL = "http://localhost/moodle/webservice/rest/server.php"
        MOODLE_TOKEN = "d7b823963e1a203d0010ecd8e7c73694"  # Usa variables de entorno en producción

        # Paso 1: Obtener cuestionarios del curso
        quizzes_params = {
            'wstoken': MOODLE_TOKEN,
            'wsfunction': 'mod_quiz_get_quizzes_by_courses',
            'moodlewsrestformat': 'json',
            'courseids[0]': course_id
        }

        try:
            # Obtener cuestionarios del curso
            quizzes_response = requests.get(MOODLE_URL, params=quizzes_params)
            quizzes_data = quizzes_response.json()

            # Manejar errores de Moodle
            if 'exception' in quizzes_data:
                return Response(
                    {"error": f"Moodle: {quizzes_data['message']}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Si no hay cuestionarios en el curso
            if not quizzes_data.get('quizzes'):
                return Response(
                    {"message": "El curso no tiene cuestionarios"},
                    status=status.HTTP_200_OK
                )
            # Paso 2: Obtener intentos del usuario en cada cuestionario
            all_attempts = []
            for quiz in quizzes_data['quizzes']:
                quiz_id = quiz['id']

                # Parámetros para obtener intentos
                attempts_params = {
                    'wstoken': MOODLE_TOKEN,
                    'wsfunction': 'mod_quiz_get_user_attempts',
                    'moodlewsrestformat': 'json',
                    'quizid': quiz_id,
                    'userid': user_id
                }

                attempts_response = requests.get(MOODLE_URL, params=attempts_params)
                attempts_data = attempts_response.json()

                if 'attempts' in attempts_data:
                    # Agregar metadata del cuestionario
                    for attempt in attempts_data['attempts']:
                        attempt['quiz_name'] = quiz['name']
                        attempt['course_id'] = course_id
                    all_attempts.extend(attempts_data['attempts'])

            return Response({
                "user_id": user_id,
                "course_id": course_id,
                "attempts": all_attempts
            })
        
        except requests.exceptions.RequestException as e:
            return Response(
                {"error": f"Error de conexión: {str(e)}"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        except Exception as e:
            return Response(
                {"error": f"Error interno: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )