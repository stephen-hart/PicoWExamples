from machine import Pin
import time
led = Pin('LED', Pin.OUT)

while(True):
    led.on()
    time.sleep(.2)
    led.off()
    time.sleep(.2)

