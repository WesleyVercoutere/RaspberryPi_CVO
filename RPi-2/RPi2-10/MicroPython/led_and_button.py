import machine
import time

led = machine.Pin(23, machine.Pin.OUT)
button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    button_value = not button.value()
    print("button_value=",button_value)
    led.value(button_value)
    time.sleep(0.1)
