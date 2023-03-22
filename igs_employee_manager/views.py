from rest_framework import viewsets
from igs_employee_manager.serializers import DepartmentsSerializer, CollaboratorsSerializer
from igs_employee_manager.models import Departments, Collaborators


class CollaboratorsViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Collaborators.objects.all()
    serializer_class = CollaboratorsSerializer



class DepartmentsViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer