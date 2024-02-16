from gpiozero import LED
import time
# Write your program below
redLed = LED(21)

redLed.on()
time.sleep(1)
redLed.off()
time.sleep(1)

redLed.on()
time.sleep(1)
redLed.off()
time.sleep(1)