from rest_framework.viewsets import ModelViewSet
from .models import Employee, TimeSheet
from .serializers import EmployeeSerializer, TimeSheetSerializer


class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class TimeSheetView(ModelViewSet):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer
