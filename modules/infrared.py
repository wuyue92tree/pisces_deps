import RPi.GPIO as GPIO


class Infrared(object):
    """
    红外避障模块
    out对应树莓派的GPIO接口
    mode为GPIO接口使用的模式
    """
    def __init__(self, out, mode=GPIO.BCM):
        GPIO.setmode(mode)
        GPIO.setup(OUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def loop(self):
        while True:
            if (GPIO.input(OUT) == 0):
                print("Detected Barrier!")
