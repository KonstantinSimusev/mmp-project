from rest_framework.serializers import ModelSerializer
from .models import Employee, TimeSheet


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class TimeSheetSerializer(ModelSerializer):
    class Meta:
        model = TimeSheet
        fields = '__all__'
