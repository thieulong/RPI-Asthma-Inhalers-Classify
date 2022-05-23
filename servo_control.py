from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

def setAngle(type, angle):
    if angle >= 90:
        value = angle / 90 - 1
    elif angle < 90:
        value = - (1 - (angle/90))
    if type == 1:
        servo1.value = value
    elif type == 2:
        servo2.value = value

factory = PiGPIOFactory()

servo1 = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo2 = Servo(27, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
