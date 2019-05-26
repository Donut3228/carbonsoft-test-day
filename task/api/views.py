from django.shortcuts import render, redirect, reverse
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
        measure_time = request.GET.get('measure_time')
        # print()

        for each in values:
            sensor = Sensor.objects.get(slug__exact=each)
            obj = SensorHistory.objects.create(value=values[each], sensor=sensor, date=measure_time)

        return response.HttpResponse()
        

# Create your views here.
