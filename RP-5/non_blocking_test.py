import RPi.GPIO as GPIO
import time

drukknop=18
led_toggle =23
led_follow=24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(drukknop,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_toggle,GPIO.OUT)
GPIO.setup(led_follow,GPIO.OUT)

tijd=time.time()  # stockeer de huidige UTC tijd in de variabele tijd
led_status=1
GPIO.output(led_toggle,led_status)

while True:    
    status_schakelaar=GPIO.input(drukknop) # status_schakelaar=1 wanneer er niet wordt gedrukt
    status_schakelaar=not status_schakelaar  # status_schakelaar=0 wanneer er niet wordt gedrukt  
    GPIO.output(led_follow,status_schakelaar) # led brandt wanneer er wordt gedrukt
    if time.time() >= tijd+1:                   # is de huidige tijd groter of gelijk aan dan de vorige tijd in de variabele + 1 seconde
        print("nu in if en time=", time.time())
        tijd = time.time()
        led_status = not led_status  # keer de inhoud van de variabele led_status om
        GPIO.output(led_toggle,led_status) # stuur de toestand in de variabele led_status naar de led

