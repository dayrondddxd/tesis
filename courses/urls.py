from rest_framework import routers
# from .api import IntegrationViewSet
from .api import CourseViewSet
# from .views import CreateUserInMoodleView
# from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
 
# router.register('api/integration', IntegrationViewSet, 'integration')
router.register('api/course', CourseViewSet, 'course')
 

urlpatterns = router.urls