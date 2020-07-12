import RPi.GPIO as GPIO


class Infrared(object):
    """
    红外避障模块
    out对应树莓派的GPIO接口
    mode为GPIO接口使用的模式
    """
    def __init__(self, out, mode=GPIO.BCM):
        self.out = out
        GPIO.setwarnings(False)
        GPIO.setmode(mode)
        GPIO.setup(self.out, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def status(self):
        if (GPIO.input(self.out) == 0):
            return True
        return False