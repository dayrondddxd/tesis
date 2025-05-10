# from django.db.models.signals import post_save
# from django.http import HttpResponse,response
# from django.dispatch import receiver
# # from django.contrib.auth.models import User
# from .models import Integration
# from courses.models import Course
# import requests


# @receiver(post_save, sender=Integration)
# def create_moodle_user(sender, instance, created, **kwargs):
#     if created:
#         moodle_url = "http://localhost/moodle/webservice/rest/server.php"
#         # token = "573a77f131d2d81a4dec40a22513a9e6"
        
#         user_data = {
#             "wstoken":"573a77f131d2d81a4dec40a22513a9e6",
#             # "wstoken": token,
#             "wsfunction": "core_user_create_users",
#             "moodlewsrestformat": "json",
#             "users[0][username]": instance.username,
#             "users[0][password]": instance.password,  # O usa una contraseña generada
#             "users[0][firstname]": instance.firstname,
#             "users[0][lastname]": instance.lastname,
#             "users[0][email]": instance.email,
#             # "auth": "manual",
#         }
        
#         params = {
#             # "wstoken": token,
#             # "wsfunction": "core_user_create_users",
#             # "moodlewsrestformat": "json",
#             # "users[23]": user_data,
#         }
#         print("SE ENVIO EL USUARIO")
#         response = requests.post(moodle_url, data=user_data)
#         # requests.post(moodle_url, data=params)


#         if response.status_code == 200:
#             moodle_response = response.json()
#             if moodle_response and isinstance(moodle_response, list):
#                 instance.userid = moodle_response[0]['id']  # Captura el ID del usuario en Moodle
#                 instance.save()
#                 print("Usuario creado en Moodle:", moodle_response)
#         else:
#             print("Error al crear usuario en Moodle:", response.text)






# import requests
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Integration

         # Matricular un usuario en un curso
# @receiver(post_save, sender=Integration )
# def enrol_user(sender , created , instance, **kwargs ):  # roleid=5  roleid 5 es "Estudiante"
#     if created:
#         moodle_url = "http://localhost/moodle/webservice/rest/server.php"
  
#          # Obtener el courseid del curso con categoryid = 1
#         course = Course.objects.filter(categoryid=1).first()
#         if not course:
#             print("No se encontró un curso con categoryid = 1")
#             return

#         enrolments = {
#          "wstoken": "573a77f131d2d81a4dec40a22513a9e6",
#          "wsfunction": "enrol_manual_enrol_users",
#          "moodlewsrestformat": "json",
#          "enrolments[0][userid]": instance.userid,
#          "enrolments[0][courseid]": course.courseid,  # ID del curso en Moodle (categoryid = 1)
#          "enrolments[0][roleid]": 5,  # Role ID para "Estudiante"
         # "enrolments[0][categoryid]": instance.Course.filter(categoryId = 1),
         # "enrolments[0][roleid]": roleid,
         # "enrolments[0][userid]": instance.id,  # Asegúrate de que `instance.id` sea el ID del usuario en Moodle
         # "enrolments[0][categoryid]": Course.categoryid(1),
         # "enrolments[0][Course.categoryid]": 2,
        # }

        #  print("SE MATRICULO EL USUARIO")
        # #  requests.post(moodle_url, data=enrolments)


        #  response = requests.post(moodle_url, data=enrolments)
        #  if response.status_code == 200:
        #      print("Usuario matriculado en el curso:", response.json())
        #  else:
        #      print("Error al matricular usuario en el curso:", response.text)












import json
import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Integration 
from courses.models import Course

# ARREGLADO
import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Integration
from courses.models import Course

@receiver(post_save, sender=Integration)
def create_moodle_user(sender, instance, created, **kwargs):
    if created:
        # 1. Crear usuario y obtener su ID de Moodle
        moodle_user_id = create_moodle_user(instance)
        if moodle_user_id:
            # 2. Matricular usuario usando el ID correcto
            enrol_user_to_course(instance, moodle_user_id)

        # create_moodle_user(instance)
        # enrol_user_to_course(instance)


def create_moodle_user(instance):

        moodle_url = "http://localhost/moodle/webservice/rest/server.php"
        user_data = {
             "wstoken": "d7b823963e1a203d0010ecd8e7c73694",
             "wsfunction": "core_user_create_users",
             "moodlewsrestformat": "json",


             "users[0][username]": instance.username,
             "users[0][password]": instance.password,
             "users[0][firstname]": instance.firstname,
             "users[0][lastname]": instance.lastname,
             "users[0][email]": instance.email,                     
         
         }
        # print("se envio el usuarion")
    
        response = requests.post(moodle_url, data=user_data)
        if response.status_code == 200:
            result = response.json()
            if result and not isinstance(result, dict):  # Si la respuesta es un array
                return result[0]['id']  # Retorna el ID del usuario en Moodle
        print("Error creando usuario:", response.text)
        return None

# @receiver(post_save, sender=Integration)
# def enrol_user(sender, instance, created, **kwargs):
#      if created:
#         moodle_url = "http://localhost/moodle/webservice/rest/server.php"
        
#         #  Obtener el ID del curso
#         # course = Course.objects.get(courseid=1)
#         # course_id = course.courseid


#          # Obtener el courseid del curso con categoryid = 1
#          # course = Course.objects.filter(categoryid=1).first()
#          # courses = Course.objects.filter(courseid=1)
#          # if not courses:
#          #     print("No se encontró un curso con courses = 1")
#          #     return
        
#         enrolments = {
#              "wstoken": "573a77f131d2d81a4dec40a22513a9e6",
#              "wsfunction": "enrol_manual_enrol_users",
#              "enrolmentmethod": "manual",
#              "moodlewsrestformat": "json",
#              "enrolments[0][userid]": instance.userid,  # Asegúrate de que este sea el ID de Moodle
#              "enrolments[0][courseid]": Course.objects.get(courseid=1).courseid,
#             #   "enrolments[0][courseid]": course_id,  # Usar el courseid del curso encontrado
#              "enrolments[0][roleid]": instance.roleid,  # Role ID para "Estudiante"
#         }
        
#         print("se envio la matricula")
        
#         response = requests.post(moodle_url, data=enrolments)
#         if response.status_code == 200:
#              print("Usuario matriculado en el curso:", response.json())
#         else:
#              print("Error al matricular usuario en el curso:", response.text)

#         print("Datos enviados a Moodle:", enrolments)
#         print("Respuesta de Moodle:", response.text)










# @receiver(post_save, sender=Integration)
# def enrol_user(sender, instance, created, **kwargs):
#     if created:

def enrol_user_to_course(instance, moodle_user_id):
        moodle_url = "http://localhost/moodle/webservice/rest/server.php"
        
            # Obtener el ID del curso
            # course = Course.objects.get(courseid=3)
            # course_id = course.courseid
        
            # Datos para la matrícula
        enrolments_data = {
                "wstoken": "d7b823963e1a203d0010ecd8e7c73694",
                "wsfunction": "enrol_manual_enrol_users",
                # "wsfunction": "enrol_self_enrol_user",
                "moodlewsrestformat": "json",
                "enrolmentmethod": "manual",
                # "enrolments":
                #   [
                    # {
                "enrolments[0]userid": moodle_user_id, 
                # "enrolments[0]courseid": Course.objects.get(courseid=3).courseid,      # ID del curso en Moodle
                "enrolments[0]courseid": 3,
                "enrolments[0]roleid": 5,  # Role ID para "Estudiante" (ej. 5)
                # ]
            }
            
        try:
            # print("MATRICULACION ENVIADa")    
            # Enviar la solicitud POST a Moodle
            response = requests.post(moodle_url, data = enrolments_data)


        # response = requests.post(moodle_url, data=enrolments_data)
            # response.raise_for_status()
            # print("Usuario matriculado en curso")
        # except requests.RequestException as e:
            # print(f"Error al matricular usuario: {e}")
                # data=json.dumps(enrolments_data),
                # headers={"Content-Type": "application/json"}
        # print("Datos enviados a Moodle:", enrolments_data)
            

        #     # Procesar la respuesta
            if response.status_code == 200:
                print("Usuario matriculado en el curso:", response.json())
            else:
                print("Error al matricular usuario en el curso:", response.text)
        
        except Course.DoesNotExist:
            print("Error: No se encontró el curso con courseid=1.")
        except requests.exceptions.RequestException as e:
            print("Error de red al conectar con Moodle:", str(e))
        except Exception as e:
            print("Error inesperado:", str(e))

            print("Datos enviados a Moodle:", enrolments_data)
            print("Respuesta de Moodle:", response.text)