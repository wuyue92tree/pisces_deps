import RPi.GPIO as GPIO
import time


class Ultrasound(object):
    """
    超声波测距模块
    trig, echo对应树莓派的GPIO接口
    mode为GPIO接口使用的模式
    """
    def __init__(self, trig, echo, mode=GPIO.BCM):
        GPIO.setmode(mode)
        GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(echo, GPIO.IN)

    def checkdist(self):
        GPIO.output(trig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trig, GPIO.LOW)
        while not GPIO.input(echo):
            pass
        t1 = time.time()
        while GPIO.input(echo):
            pass
        t2 = time.time()
        return (t2-t1) * 340 / 2
