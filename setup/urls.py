from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from igs_employee_manager.views import CollaboratorsViewSet, DepartmentsViewSet

router = routers.DefaultRouter()
router.register('collaborators', CollaboratorsViewSet)
router.register('departments', DepartmentsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
