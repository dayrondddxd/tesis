
########SEÑAL PARA CURSOS#######
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course
import requests

MOODLE_URL = "http://localhost/moodle/webservice/rest/server.php"
# MOODLE_TOKEN = "573a77f131d2d81a4dec40a22513a9e6"

@receiver(post_save, sender=Course)
def sync_course_to_moodle(sender, instance, created, **kwargs):
    if created:  # Solo para nuevos cursos
        data = { 
            "wstoken": "d7b823963e1a203d0010ecd8e7c73694",
            "wsfunction": "core_course_create_courses",
            "moodlewsrestformat": "json",
            "courses[0][fullname]": instance.fullname,
            "courses[0][shortname]": instance.shortname,
            "courses[0][categoryid]": instance.categoryid,
            # "courses[0][qualification]": instance.qualification,
            # "courses[0][complete]": instance.complete,
        }
        print("SE ENVIO EL CURSO")
        response = requests.post(MOODLE_URL, data=data)
        result = response.json()
        
        # if not isinstance(result, list) and result.get('exception'):
        #     raise Exception(f"Error de Moodle: {result.get('message')}")
        
        # # Actualizar el curso con el ID de Moodle
        # if created and result:
        #     instance.moodle_id = result[0]['id']
        #     instance.save(update_fields=['moodle_id'])

        # Actualizar el curso con el ID de Moodle
        # if not isinstance(result, list) and result.get('exception'):
        #     raise Exception(f"Error de Moodle: {result.get('message')}")
        
        # if created and result:
        #     instance.courseid = result[0]['id']
        #     instance.save(update_fields=['courseid'])
