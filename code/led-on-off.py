from gpiozero import LED
import time
# Write your program below
redLed = LED(21)

for x in range(3):
    redLed.on()
    time.sleep(1)
    redLed.off()
    time.sleep(1)