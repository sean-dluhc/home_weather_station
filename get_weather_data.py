import sys
import Adafruit_DHT

while True:
    humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 18)
    if humidity is not None and temp is not None:
        print('Temperature = {0:0.1f}* Humidity = {1:0.1f}%'.format(temp, humidity))