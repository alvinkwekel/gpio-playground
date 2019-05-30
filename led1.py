from gpiozero import LED
from time import sleep

led_blauw = LED(17)
led_rood = LED(18)

while True:
    led_blauw.on()
    led_rood.off()
    sleep(0.4)
    led_blauw.off()
    led_rood.on()
    sleep(0.1)
