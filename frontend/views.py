import time
import datetime
import random
import json
from django.shortcuts import render
from api.models import temp_log
from api.serializers import tempSerializer
import datetime

date = '2022-03-28T22:40:41.730193+05:30'
date = date.split(".")[0]
datem = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
print(datem.day)


def index(request):
    context = {}
    context['temp'] = 0
    context['humidity'] = 0
    return render(request, 'home.html', context)


def linechart(request):
    """
    lineChart page
    """

    context = {}
    queryset = temp_log.objects.all().order_by('-id')
    ser = tempSerializer(queryset, many=True)
    first = ser.data[0]["time"]
    date = first.split(".")[0]
    f_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S').day

    arr = [['Time', 'Temperature']]

    for i in ser.data:
        date = i["time"].split(".")[0]
        datem = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        if f_date == datem.day:
            time = (datem.hour * 60) + datem.minute - 60
            arr.append([time, i["temp"]])

    context['temp'] = json.dumps(arr)
    print(context['temp'])

    return render(request, 'linechart.html', context)
