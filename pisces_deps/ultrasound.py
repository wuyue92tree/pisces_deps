import RPi.GPIO as GPIO
import time


class Ultrasound(object):
    """
    超声波测距模块HC-SR04
    trig, echo对应树莓派的GPIO接口
    mode为GPIO接口使用的模式
    """
    def __init__(self, trig, echo, mode=GPIO.BCM):
        self.trig = trig
        self.echo = echo
        GPIO.setwarnings(False)
        GPIO.setmode(mode)
        GPIO.setup(self.trig, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.echo, GPIO.IN)

    def checkdist(self):
        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trig, GPIO.LOW)
        while not GPIO.input(self.echo):
            pass
        t1 = time.time()
        while GPIO.input(self.echo):
            pass
        t2 = time.time()
        return (t2-t1) * 340 / 2