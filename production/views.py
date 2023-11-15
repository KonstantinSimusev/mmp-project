from rest_framework.viewsets import ModelViewSet
from .serializers import AreaSerializer, ReportSerializer, ProfessionSerializer
from .models import Area, Report, Profession


class AreaView(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class ReportView(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ProfessionView(ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
