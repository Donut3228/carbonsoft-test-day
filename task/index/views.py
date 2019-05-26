import json
import urllib.request
from builtins import object

from django.http import HttpRequest
from django.shortcuts import redirect, render, reverse

from api import models
from api import views as api_views


def index(request):
    sensors = models.Sensor.objects.all()

    context = {'sensors': sensors}
    return render(request, template_name='index.html', context=context)


def sensor_item(request, slug):
    data = models.SensorHistory.objects.filter(sensor__slug=slug)
    sensor = models.Sensor.objects.get(slug__exact=slug)
    item = data[0]

    context = {'slug': slug, 'data': data, 'item': item}
    return render(request, template_name="sens_item.html", context=context)


def sens_item_edit(request, pk):
    item = models.SensorHistory.objects.get(pk=pk)

    item_name = 'Item ' + str(item.id) + ' edit'
    breadcrumb = [{'name': item.sensor.name, 'link': 'sens_item'},
                  {'name': item_name, 'link': 'sens_item_edit', 'args': item.id}]

    if request.method == 'POST':
        item.value = request.POST['item_val']
        item.save()

        return redirect(reverse('sens_item', kwargs={"slug": item.sensor.slug}))

    context = {'item': item, 'bread_items': breadcrumb}

    return render(request, template_name="sens_item_edit.html", context=context)


def sens_item_del(request, pk):
    item = models.SensorHistory.objects.get(pk=pk)

    item_name = 'Item ' + str(item.id) + ' delete'
    breadcrumb = [{'name': item.sensor.name, 'link': 'sens_item'},
                  {'name': item_name, 'link': 'sens_item_edit', 'args': item.id}]

    if request.method == 'POST':
        item.delete()
        return redirect(reverse('sens_item', kwargs={"slug": item.sensor.slug}))

    context = {'item': item, 'bread_items': breadcrumb}

    return render(request, template_name='sens_item_del.html', context=context)
