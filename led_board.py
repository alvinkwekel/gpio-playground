from gpiozero import LEDBoard
from time import sleep

leds = LEDBoard(26, 19, 13, 6, 5)

while True:
    
    leds.value = (1, 0, 0, 0, 0)
    sleep(.1)
    leds.value = (0, 1, 0, 0, 0)
    sleep(.1)
    leds.value = (0, 0, 1, 0, 0)
    sleep(.1)
    leds.value = (0, 0, 0, 1, 0)
    sleep(.1)
    leds.value = (0, 0, 0, 0, 1)
    sleep(.1)

    leds.value = (0, 0, 0, 0, 1)
    sleep(.1)
    leds.value = (0, 0, 0, 1, 0)
    sleep(.1)
    leds.value = (0, 0, 1, 0, 0)
    sleep(.1)
    leds.value = (0, 1, 0, 0, 0)
    sleep(.1)
    leds.value = (1, 0, 0, 0, 0)
    sleep(.1)
