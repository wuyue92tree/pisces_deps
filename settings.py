import RPi.GPIO as GPIO

car_config = {
  'ena': 16,
  'int1': 20,
  'int2': 21,
  'enb': 22,
  'int3': 17,
  'int4': 27,
  'mode': GPIO.BCM
}

infrared_config = {
  'out': 25,
  'mode': GPIO.BCM
}

ultrasound_config = {
  'trig': 24,
  'echo': 23,
  'mode': GPIO.BCM
}