import json
import urllib.request
from builtins import object

from django.http import HttpRequest
from django.shortcuts import redirect, render, reverse

from api import models
from api import views as api_views


breadcrumb = {'HOME': 'index'}


def breadcrumb_dict(*args):
    
    result = {}
    for each in args:
        for i in each:
            result[i] = each[i]

    return result



def index(request):

    sensors = models.Sensor.objects.all()
    global breadcrumb
    if len(breadcrumb) > 1:
        breadcrumb = {'HOME': 'index'}

    
    bc = breadcrumb_dict({'HOME': 'index'})

    context = {'sensors': sensors, 'breadcrumb': breadcrumb, 'bc': bc}
    return render(request, template_name='index.html', context=context)


def sensor_history(request, slug):
    data = models.SensorHistory.objects.filter(sensor__slug=slug)
    sensor = models.Sensor.objects.get(slug__exact=slug)

    global breadcrumb

    breadcrumb = {'HOME': 'index', sensor.name: 'sens_item'}

    context = {'slug': slug, 'data': data, 'breadcrumb': breadcrumb}
    return render(request, template_name="sens_item.html", context=context)


def sens_item_edit(request, pk, slug):
    item = models.SensorHistory.objects.get(pk=pk)
    sensor = item.sensor
    if request.method == 'POST':
        item.value = request.POST['item_val']

        item.save()

        return redirect(reverse('sens_item', kwargs={"slug": sensor.slug}))

    global breadcrumb
    item_name = 'Item ' + str(item.id) + ' edit'
    breadcrumb = {'HOME': 'index', sensor.name: 'sens_item',
                  item_name: 'sens_item_edit'}

    context = {'item': item, 'breadcrumb': breadcrumb, 'slug': slug}

    return render(request, template_name="sens_item_edit.html", context=context)


def sens_item_del(request, pk, slug):
    item = models.SensorHistory.objects.get(pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect(reverse('sens_item', kwargs={"slug": item.sensor.slug}))

    global breadcrumb
    item_name = 'Item ' + str(item.id) + ' delete'
    breadcrumb = {'HOME': 'index', item.sensor.name: 'sens_item',
                  item_name: 'sens_item_edit'}
    breadcrumb[item_name] = 'sens_item_del'

    context = {'item': item, 'slug': slug, 'breadcrumb': breadcrumb}
    return render(request, template_name='sens_item_del.html', context=context)
