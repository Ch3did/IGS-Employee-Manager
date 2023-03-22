from rest_framework import serializers
from igs_employee_manager.models import Collaborators, Departments

    
class CollaboratorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collaborators
        fields = '__all__'


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields = '__all__'

