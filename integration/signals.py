from django.db.models.signals import post_save
from django.http import HttpResponse
from django.dispatch import receiver
# from django.contrib.auth.models import User
from .models import Integration
import requests


import requests

@receiver(post_save, sender=Integration)
def create_moodle_user(sender, instance, created, **kwargs):
    if created:
        moodle_url = "http://localhost/moodle/webservice/rest/server.php"
        # token = "573a77f131d2d81a4dec40a22513a9e6"
        
        user_data = {
            "wstoken":"573a77f131d2d81a4dec40a22513a9e6",
            # "wstoken": token,
            "wsfunction": "core_user_create_users",
            "moodlewsrestformat": "json",
            "users[0][username]": instance.username,
            "users[0][password]": instance.password,  # O usa una contraseña generada
            "users[0][firstname]": instance.firstname,
            "users[0][lastname]": instance.lastname,
            "users[0][email]": instance.email,
            # "auth": "manual",
        }
        
        params = {
            # "wstoken": token,
            # "wsfunction": "core_user_create_users",
            # "moodlewsrestformat": "json",
            # "users[23]": user_data,
        }
        print("SE ENVIO EL USUARIO")
        requests.post(moodle_url, data=user_data)
        # requests.post(moodle_url, data=params)

        # if response.status_code == 200:
        #     print("Usuario creado en Moodle:", response.json())
        # else:
        #     print("Error al crear usuario en Moodle:", response.text)








# #QWEN
# # signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# import requests

# @receiver(post_save, sender=User)
# def create_moodle_user(sender, instance, created, **kwargs):
#     if created:
#         moodle_url = "http://localhost/moodle/webservice/rest/server.php"
#         token = "573a77f131d2d81a4dec40a22513a9e6"
        
#         user_data = {
#             "username": sender.username,
#             "password": "default_password",  # O usa una contraseña generada
#             "firstname": instance.first_name,
#             "lastname": instance.last_name,
#             "email": instance.email,
#             "auth": "manual",
#         }
        
#         params = {
#             "wstoken": token,
#             "wsfunction": "core_user_create_users",
#             "moodlewsrestformat": "json",
#             "users[0]": user_data,
#         }
        
#         requests.post(moodle_url, data=params)
























# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# import requests
# from rest_framework import settings

# @receiver(post_save, sender=User)
# def create_moodle_user(sender, instance, created, **kwargs):
#     if created:
#         # Configurar los parámetros para Moodle
#         data = {
#             'wstoken': settings.MOODLE_API_TOKEN,
#             'wsfunction': 'core_user_create_users',
#             'moodlewsrestformat': 'json',
#             'users[0][username]': instance.username,
#             'users[0][password]': "ContrasenaTemporal123!",  # Personaliza esto
#             'users[0][firstname]': instance.first_name,
#             'users[0][lastname]': instance.last_name,
#             'users[0][email]': instance.email,
#             'users[0][auth]': 'manual',
#             'users[0][mailformat]': 1,
#         }

#         # Enviar solicitud a Moodle
#         response = requests.post(settings.MOODLE_API_URL, data=data)
        
#         if response.status_code == 200:
#             print("Usuario creado en Moodle:", response.json())
#         else:
#             print("Error:", response.text)