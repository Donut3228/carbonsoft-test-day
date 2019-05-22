from rest_framework import serializers
from .models import Sensor, SensorHistory


class SensorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sensor
        fields = ('url', 'name', 'min_value', 'max_value', 'slug')



class SensorHistorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SensorHistory
        fields = ('url', 'date', 'value', 'sensor')