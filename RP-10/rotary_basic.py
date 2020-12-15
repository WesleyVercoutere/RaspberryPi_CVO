import RPi.GPIO as GPIO
import time


enc_A = 20
enc_B = 16
enc_schak = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(enc_A, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(enc_B, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)

status_enc_A = False
status_enc_A_before = False
status_enc_B = False
status_enc_B_before = False

teller=0

print("Start testing!")

while True:
    # check if enc_A changes
    status_enc_A = GPIO.input(enc_A)
    if status_enc_A != status_enc_A_before:
        status_enc_A_before = status_enc_A
        if status_enc_A:  # is A flank stijgend?
            status_enc_B = GPIO.input(enc_B)
            if status_enc_B: # is B hoog
                teller-=1
            else: # dan is B laag
                teller+=1            
            print(teller)
