import time

import machine

led = machine.Pin(23, machine.Pin.OUT)

while True:
    
    led.value(1)
    time.sleep(0.001)
    led.value(0)
    time.slee(0.001)
    
    

