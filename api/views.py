# from rest_framework import viewsets


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import temp_log
import requests
import datetime
from .broadcast import transmit
from .serializers import tempSerializer, broadcast_ser
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


class tempViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = tempSerializer

    def get(self, request):
        queryset = temp_log.objects.all().order_by('-id')
        serializer = self.serializer_class(queryset, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        ser = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        if ser.is_valid():
            ser.save()

        return Response(data=ser.data)

    def delete(self, request):
        temp_log.objects.all().delete()
        return Response(data={"message": "Deleted"})


class tempassistViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = tempSerializer

    def get(self, request):
        queryset = temp_log.objects.all().order_by('-id')
        serializer = self.serializer_class(queryset, many=True)

        return Response(data=serializer.data[0])


class chartapi(APIView):
    def get(self, request):
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
        return Response(data={"array": arr})


class fmview(APIView):
    serializer_class = broadcast_ser

    def get(self, request):
        return Response({"status": "OK"})

    def post(self, request):
        ser = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        if ser.is_valid():
            ser.validated_data
            return Response(data=ser.validated_data)
        return Response({"status": "OK"})
