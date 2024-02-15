from robot import *
from machine import LED

led = LED("LED_BLUE")
led.on()

thresholds = [
              (30, 60, 10, 40, 10, 40),   # Broader Red
              (50, 80, -25, 10, 30, 60),   # Broader Yellow
]

robot = Robot(thresholds)

robot.stage1(0.3, 0.5)
