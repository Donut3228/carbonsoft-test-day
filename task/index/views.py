from django.shortcuts import render, redirect, reverse
import urllib.request
import json
from api import models
from api import views as api_views
from django.http import HttpRequest


def index(request):

    sensors = models.Sensor.objects.all()

    # sens_hist_last = models.SensorHistory.objects

    context = {'sensors': sensors}
    return render(request, template_name='index.html', context=context)
# Create your views here.


def sensor_history(request, slug):
    data = models.SensorHistory.objects.filter(sensor__slug=slug)

    context = {'slug': slug, 'data': data}
    return render(request, template_name="sens_item.html", context=context)


def sens_item_edit(request, pk):
    item = models.SensorHistory.objects.get(pk=pk)
    sensor = item.sensor
    if request.method == 'POST':
        item.value = request.POST['item_val']

        item.save()

        return redirect(reverse('sens_item', kwargs={"slug": sensor.slug}))

        context = {'item': item}
    return render(request, template_name="sens_item_edit.html", context=context)


def sens_item_del(request, pk):

    item = models.SensorHistory.objects.get(pk=pk)

    item.delete()

    return redirect(reverse('sens_item', kwargs={"slug": item.sensor.slug}))
    return redirect()
