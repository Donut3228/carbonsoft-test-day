from django.shortcuts import render
from django.http import response
from rest_framework import viewsets
from .models import Sensor, SensorHistory
from .serializers import SensorSerializer, SensorHistorySerializer
import json

class SensorViewSet(viewsets.ModelViewSet):

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorHistoryViewSet(viewsets.ModelViewSet):

    queryset = SensorHistory.objects.all()
    serializer_class = SensorHistorySerializer

    def create(self, request):
        values = request.data
        sensor = Sensor.objects.get(slug__exact=values['slug'])
        obj = SensorHistory.objects.create(value=values['value'], sensor=sensor)
        return response.HttpResponse()
        

# Create your views here.
