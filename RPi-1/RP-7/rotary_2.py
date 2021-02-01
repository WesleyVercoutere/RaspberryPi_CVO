import RPi.GPIO as GPIO
import time



enc_A = 16
enc_B = 20
enc_schak = 21

teller=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(enc_A, GPIO.IN , pull_up_down = GPIO.PUD_UP)
GPIO.setup(enc_B, GPIO.IN , pull_up_down = GPIO.PUD_UP)

status_enc_A = True
status_enc_A_before = True
status_enc_B = True
status_enc_B_before = True

print("Start testing!")
while True:
    # check if enc_A changes
    status_enc_A = GPIO.input(enc_A)
    if status_enc_A != status_enc_A_before:
        status_enc_A_before =status_enc_A
        #print("status_enc_A changed",status_enc_A)
        if status_enc_A==0:
            if GPIO.input(enc_B)==0:
                teller+=1
                print("cw", teller)
            else:
                teller-=1
                print("acw", teller)
        #time.sleep(0.002)

