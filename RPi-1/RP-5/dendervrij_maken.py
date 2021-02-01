import RPi.GPIO as GPIO
import time

drukknop=18
led_toggle =23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(drukknop,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_toggle,GPIO.OUT)
toestand_drukknop_vorige = 0
status_led=0
teller=0


while True:
    toestand_nu = GPIO.input(drukknop)
    if toestand_drukknop_vorige != toestand_nu:
        toestand_drukknop_vorige=toestand_nu
        #print("verandering gededecteerd")
        if toestand_nu==0:
           #print("u drukt de schak in")
           status_led = not status_led
           GPIO.output(led_toggle,status_led)
           teller +=1
           print("teller=",teller)
        time.sleep(0.05)
        
        
        
