from rest_framework.serializers import ModelSerializer
from .models import Area, Report, Profession


class AreaSerializer(ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class ProfessionSerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'
