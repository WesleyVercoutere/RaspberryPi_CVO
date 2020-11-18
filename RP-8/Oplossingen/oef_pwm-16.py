import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
red = 23
GPIO.setup(red, GPIO.OUT)

p = GPIO.PWM(red, 50)  # channel=23 frequency=50Hz
p.start(0)

try:
    while 1:
        for dc in range(0, 101):
            p.ChangeDutyCycle(dc)
            time.sleep(0.02)
        for dc in range(100, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.02)
        time.sleep(2)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
