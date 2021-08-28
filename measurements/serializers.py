# TODO: опишите сериализаторы
from rest_framework import serializers

from measurements.models import Project, Measurement


class ProjectModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class MeasurementModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"