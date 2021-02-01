import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


#GPIO.setup(23,GPIO.IN)
#GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Druk CTRL C om dit programma te beëindigen!")

while True:
    print("Input GPIO23 is nu ",GPIO.input(23))
    time.sleep(0.25)
