import RPi.GPIO as GPIO
import time


enc_A = 16
enc_B = 20
enc_schak = 21

status_enc_A_before = True
status_enc_B_before = True

teller=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(enc_A, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(enc_B, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)


def fct_enc_A(pin_nr):
    global teller
    #time.sleep(0.05)
    hulp=GPIO.input(enc_B)
    print(hulp)
    if hulp == 1 :
        teller-=1
    else:
        teller+=1
    #print(teller)


GPIO.add_event_detect(enc_A, GPIO.RISING, callback = fct_enc_A)

teller=0
teller_before=0

print("Start testing callback!")
while True:
    pass
    '''
    if teller_before != teller:
        teller_before=teller
        #print(teller)
    
'''






