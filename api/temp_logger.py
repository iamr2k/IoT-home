import requests
from asgiref.sync import sync_to_async
import time
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


last_temp = 0

# @sync_to_async


def auto_updator():
    last_temp = 0
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            pass
        else:
            temperature = 0
            humidity = 0
        resp = {"temp": round(temperature, 2),
                "humidity": round(humidity, 2)}
        requests.post('http://localhost/api/', data=resp)
        time.sleep(120)


auto_updator()
