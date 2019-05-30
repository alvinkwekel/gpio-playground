from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:

    led.value = 0.3  # half brightness
    sleep(1)
    led.value = 1  # full brightness
    sleep(1)

