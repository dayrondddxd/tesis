# import requests
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Integration
# # 
# class MoodleEnrollmentView(APIView):
#     def post(self, request):
#         moodle_url = "https://localhost/moodle/webservice/rest/server.php"
#     token = "573a77f131d2d81a4dec40a22513a9e6"
        
#         # moodle_url = "https://tu-moodle.com/webservice/rest/server.php"
#         # MOODLE_URL = "localhost/moodle/webservice/rest/server.php"

# #         # token = "TU_TOKEN_MOODLE"
# #         # Ficha o Token de Moodle = '573a77f131d2d81a4dec40a22513a9e6'

# #         # Datos del usuario y curso
#     user_data = {
#             'username': requests.data['username'],
#             'password': requests.data['password'],
#             'firstname': requests.data['firstname'],
#             'lastname ': requests.data['lastname'],
#             'email': requests.data['email'],
#             # /... otros campos
#     }
        
#     # Crear usuario en Moodle
#     response = requests.post(
#             moodle_url,
#             data={
#                 'wstoken': token,
#                 'wsfunction': 'core_user_create_users',
#                 'users[0]': user_data,
#                 'moodlewsrestformat': 'json'
#             }
#         )
        
    #     # Matricular en curso
    #     if response.status_code == 200:
    #         enrol_data = {
    #             'enrolments[0][userid]': response.json()[0]['id'],
    #             'enrolments[0][courseid]': request.data['course_id'],
    #         }
    #         requests.post(
    #             moodle_url,
    #             data={
    #                 'wstoken': token,
    #                 'wsfunction': 'enrol_manual_enrol_users',
    #                 **enrol_data,
    #                 'moodlewsrestformat': 'json'
    #             }
    #         )
        
    #     return Response(response.json())
