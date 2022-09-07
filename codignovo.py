import RPi.GPIO as gpio
import time


class Sensor(object):
    def __init__(self, trig = 0, echo = 0, name = "Name"):
        self.trig = trig
        self.echo = echo
        self.name = name

        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        gpio.setup(self.trig, gpio.OUT)
        gpio.setup(self.echo, gpio.IN)

        gpio.output(self.trig, False)

        print ("Waiting For Sensor To Settle")
        time.sleep(1)


    def sense(self):
        gpio.output(self.trig, True)
        time.sleep(0.00001)
        gpio.output(self.trig, False)

        start = time.time()
        while gpio.input(self.echo) == 1:
            pass
        end = time.time()

        duration = end - start
        distance = duration * 17150

        return round(distance, 2)

    def end(self):
        gpio.cleanup()
                
sensor_1=Sensor(24, 25, "Front")
while True:
            mm = sensor_1.sense()
            time.sleep(0.2)
            print(mm)

