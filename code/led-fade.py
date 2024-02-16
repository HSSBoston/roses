from gpiozero import PWMLED
import time
# Write your program below

ledValueDelta = 0.005
interval = 0.01

led = PWMLED(21)

while True:
    try:
        while True:
            try:
                newIntensity = led.value + ledValueDelta
                if newIntensity <= 1:
                    led.value = newIntensity
                    time.sleep(interval)
                else:
                    break
            except KeyboardInterrupt:
                break

        led.on()
        time.sleep(2)    
        for x in range(5):
            led.value = 0.0
            time.sleep(0.5)
            led.value = 0.9
            time.sleep(0.5)
            
        time.sleep(2)
        while True:
            try:
                newIntensity = led.value - ledValueDelta
                if newIntensity >= 0:
                    led.value = newIntensity
                    time.sleep(interval)
                else:
                    break
            except KeyboardInterrupt:
                break
        led.off()
        time.sleep(2)
    except KeyboardInterrupt:
        break

led.off()
