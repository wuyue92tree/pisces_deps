from RPi import GPIO


class Car(object):
    """
    基于L298N双桥电机驱动板
    ena, int1, int2, enb, int3, int4分别对应树莓派的GPIO接口
    mode为GPIO接口使用的模式
    """
    def __init__(self, ena, int1, int2, enb, int3, int4, mode=GPIO.BCM):
        GPIO.setmode(mode)
        GPIO.setup(ena, GPIO.OUT)
        GPIO.setup(enb, GPIO.OUT)
        GPIO.setup(int1, GPIO.OUT)
        GPIO.setup(int2, GPIO.OUT)
        GPIO.setup(int3, GPIO.OUT)
        GPIO.setup(int4, GPIO.OUT)

        self.pwm_left = GPIO.PWM(ena, 80)
        self.pwm_left.start(0)
        self.pwm_right = GPIO.PWM(enb, 80)
        self.pwm_right.start(0)

        self.motor_left = [int3, int4]
        self.motor_right = [int1, int2]

        # 电机速度
        self.base_speed = 0
        self.left_rate = 1
        self.right_rate = 1

    def __del__(self):
        self.pwm_left.stop()
        self.pwm_right.stop()
        GPIO.cleanup()

    @staticmethod
    def __motor_forward(motor):
        # 控制电机转动，下面两个类似，省去了实现
        GPIO.output(motor[0], GPIO.HIGH)
        GPIO.output(motor[1], GPIO.LOW)
    
    @staticmethod
    def __motor_backward(motor):
        GPIO.output(motor[0], GPIO.LOW)
        GPIO.output(motor[1], GPIO.HIGH)

    @staticmethod
    def __motor_stop(motor):
        GPIO.output(motor[0], GPIO.LOW)
        GPIO.output(motor[1], GPIO.LOW)

    def forward(self):
        Car.__motor_forward(self.motor_left)
        Car.__motor_forward(self.motor_right)

    def backward(self):
        Car.__motor_backward(self.motor_left)
        Car.__motor_backward(self.motor_right)

    def stop(self):
        self.reset_status()
        Car.__motor_stop(self.motor_left)
        Car.__motor_stop(self.motor_right)

    def left(self, rate):
        """
        左转弯的时候，右边轮胎速度不变，左边速度为右边速度 * rate
        rate值为0到1之间
        """
        self.right_rate = rate

    def right(self, rate):
        self.left_rate = rate

    def speed(self, val):
        self.base_speed = val
        self.pwm_left.ChangeDutyCycle(val * self.left_rate)
        self.pwm_right.ChangeDutyCycle(val * self.right_rate)

    def reset_status(self):
        self.base_speed = 0
        self.left_rate = 1
        self.right_rate = 1

    def get_status(self):
        return self.base_speed, \
            self.base_speed * self.left_rate, \
            self.base_speed * self.right_rate
