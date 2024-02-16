from gpiozero import PWMLED
import time
# Write your program below

led = PWMLED(21)

led.on()
time.sleep(2)

led.value = 0.75
time.sleep(2)

led.value = 0.5
time.sleep(2)

led.value = 0.25
time.sleep(2)

led.off()