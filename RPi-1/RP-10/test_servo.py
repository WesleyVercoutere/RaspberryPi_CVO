import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(21, 50)

while 1:

    p.start(2.5) # helemaal links?
    time.sleep(2)

    p.start(7.5) #midden?
    time.sleep(2)

    p.start(11.75) # helemaal rechts?
    time.sleep(2)
    
    print("test2")

