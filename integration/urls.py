from rest_framework import routers
from .api import IntegrationViewSet
from django.urls import path  # Añade esta importación
from .views import MoodleCompletedCourses
#from . import views  # Importa el módulo views de tu app
# from .views import CourseSerializer
# from .views import CreateUserInMoodleView
# from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register('api/integration', IntegrationViewSet, 'integration')
# router.register('api/courses', CourseSerializer, 'course')



urlpatterns = [
    path('completed-courses/<int:user_id>/', MoodleCompletedCourses.as_view(), name='completed-courses'),
]
# router.register("create-moodle-user/", CreateUserInMoodleView.as_view(), 'create-moodle-user')
# router.register('api/create-moodle-user', CreateUserInMoodleView, 'create-moodle-user')

# urlpatterns = router.urls

urlpatterns += router.urls

# # QWEN
# urls.py
# from django.urls import path
# from .api import CreateUserInMoodleViewSet
# from .views import CreateUserInMoodleView

# urlpatterns = [
#     path("api/create-moodle-user/", CreateUserInMoodleView.as_view(), name="create-moodle-user"),
    # path('api/integration', IntegrationViewSet.as_view(), name='integration')
# ]


