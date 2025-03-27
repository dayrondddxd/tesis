from django.shortcuts import render

# views.py
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


        # try:    
        # # 3. Crea el usuario en Moodle
        #     moodle_response = create_moodle_user(
        #         username=user.username, 
        #         password=request.data.get("password"), # Campo temporal (no guardes contraseñas en texto plano)
        #         #password=user.password,             # password=request.data.get("password"), 
        #         firstname=user.first_name,
        #         lastname=user.last_name,
        #         email=user.email,
        #     )
        
        #     # 4. Maneja errores de Moodle
        #     if "exception" in moodle_response:
        #         user.delete()  # Rollback si falla
        #         return Response(
        #             {"error": "Error en Moodle: " + moodle_response["message"]},
        #             status=status.HTTP_502_BAD_GATEWAY,
        #         )
            
        #     # 5. Opcional: Guarda el ID de Moodle en tu modelo
        #     user.moodle_id = moodle_response[19]["id"]
        #     user.save()

        #     return Response(serializer.data, status=status.HTTP_201_CREATED)

        # except Exception as e:
        #         user.delete()  # Rollback
        #         return Response(
        #             {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        #         )


























































# # views.py
# import requests
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status




# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from .deepseek import create_moodle_user


# from .models import User,Integration  # Tu modelo de usuario local
# from .serializers import IntegrationSerializer  # Tu serializer

# class UserCreateView(APIView):
#     def post(self, request):
#         # 1. Valida los datos del usuario en tu API
#         serializer = IntegrationSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # 
#         # 2. Guarda el usuario en tu base de datos
#         user = serializer.save()

# class CreateUserInMoodleView(APIView):
#     def post(self, request, *args, **kwargs):
#         # URL del servicio web de Moodle
#         moodle_url = "http://localhost/moodle/webservice/rest/server.php"  # [[4]]
#         token = "573a77f131d2d81a4dec40a22513a9e6"  # Reemplaza con tu token
        

        
#         # Parámetros para la API de Moodle
#         params = {
#             "wstoken": token,
#             "wsfunction": "core_user_create_users",  # Función para crear usuarios [[4]]
#             "moodlewsrestformat": "json",
#             "users[3]": user_data,  # Moodle espera un array de usuarios
#         }

#         # Datos del usuario (ajusta según tu modelo de Django)
#         user_data = {    
#             # "username": request.data.get("username"),
#             "username":User.username,
#             "password": request.data.get("password"),
#             "firstname": request.data.get("first_name"),
#             "lastname": request.data.get("last_name"),
#             "email": request.data.get("email"),
#             "auth": "manual",  # Método de autenticación de Moodle [[3]]
#         }


# #   {
#     # "id": 5,
#     # "username": "dayrondd"
# #   }


#         try:
#             # Envía la solicitud POST a Moodle
#             response = requests.post(moodle_url, data=params)
#             response.raise_for_status()  # Lanza error si hay un fallo HTTP
            
#             # Respuesta de Moodle (devuelve el ID del usuario creado)
#             return Response(response.json(), status=status.HTTP_201_CREATED)
        
#         except requests.exceptions.RequestException as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)