import requests
# import json

# Configuración
# MOODLE_URL = "https://tusitio.com/webservice/rest/server.php"

MOODLE_URL = "http://localhost/moodle/webservice/rest/server.php"

# Ficha o Token de Moodle = '573a77f131d2d81a4dec40a22513a9e6'
# # TOKEN = "tu_token_de_seguridad"
TOKEN = '573a77f131d2d81a4dec40a22513a9e6'



def create_moodle_user(username, password, firstname, lastname, email):
    data = {
        "wstoken": TOKEN,
        "wsfunction": "core_user_create_users",
        "moodlewsrestformat": "json",
        "users[0][username]": username,
        "users[0][passwoord]": password,  # Contraseña por defecto
        "users[0][firstname]": firstname,
        "users[0][lastname]": lastname,
        "users[0][email]": email,
    }

    response = requests.post(MOODLE_URL, data=data)
    return response.json()

    # return call_moodle_api("core_user_create_users", data)

# Matricular en curso (ID del curso local)
# def enrol_user(userid, courseid=2):  # Ajusta el ID de tu curso local
#     data = {
#         "enrolments[0][userid]": userid,
#         "enrolments[0][courseid]": courseid,
#         "enrolments[0][roleid]": 5,  # 5 = Estudiante
#     }
#     return call_moodle_api("enrol_manual_enrol_users", data)

# Uso
# if __name__ == "__main__":
#     # Crear usuario
#     new_user = create_user("juan_local", "Juan", "Pérez", "juan@local.com")
#     user_id = new_user[0]["id"]
    
    # Matricular en curso (ej: curso con ID=2)
    # enrol_user(user_id, 2)
    
    # Crear grupo y asignar (similar al ejemplo anterior)








































# OTRA VIA
# Función para llamar a la API de Moodle
# def call_moodle_api(function, data):
#     data.update({
#         "wstoken": TOKEN,
#         "moodlewsrestformat": "json",
#         "wsfunction": function
#     })
#     response = requests.post(MOODLE_URL, data=data)
#     return response.json()

# Crear un usuario
# def create_user(username, password, firstname, lastname, email):
# def create_user(user,correo):

#     users = {
#          "users[0][user]": user,
#          "users[0][correo]": correo,
        # "users[0][username]": username,
        # "users[0][password]": password,
        # "users[0][firstname]": firstname,
        # "users[0][lastname]": lastname,
        # "users[0][email]": email,
    # }
    # return call_moodle_api("core_user_create_users", users)

# Matricular un usuario en un curso
# def enrol_user(userid, courseid, roleid=5):  # roleid 5 es "Estudiante"
#     enrolments = {
#         "enrolments[0][userid]": userid,
#         "enrolments[0][courseid]": courseid,
#         "enrolments[0][roleid]": roleid,
#     }
#     return call_moodle_api("enrol_manual_enrol_users", enrolments)

# # Crear un grupo en un curso
# def create_group(courseid, name):
#     groups = {
#         "groups[0][courseid]": courseid,
#         "groups[0][name]": name,
#     }
#     return call_moodle_api("core_group_create_groups", groups)

# # Agregar un usuario a un grupo
# def add_user_to_group(userid, groupid):
#     members = {
#         "members[0][userid]": userid,
#         "members[0][groupid]": groupid,
#     }
#     return call_moodle_api("core_group_add_group_members", members)

# # Ejemplo de uso
# if __name__ == "__main__":
#     # Crear un usuario
#     user = create_user("estudiante1", "password123", "Juan", "Pérez", "juan@example.com")
#     userid = user[0]["id"]

#     # Matricular al usuario en un curso (ID del curso = 2)
#     enrol_user(userid, 2)

#     # Crear un grupo en el curso (ID del curso = 2)
#     group = create_group(2, "Grupo A")
#     groupid = group[0]["id"]

#     # Agregar el usuario al grupo
#     add_user_to_group(userid, groupid)