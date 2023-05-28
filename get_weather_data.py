import sys
import Adafruit_DHT


def get_data():
        humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 18)
        if humidity is not None and temp is not None:
            display_string = 'Temperature = {0:0.1f}C Humidity = {1:0.1f}%'.format(temp, humidity)
            print(display_string)
            return(display_string)

if __name__ == '__main__': 
    while True:
        get_data()
