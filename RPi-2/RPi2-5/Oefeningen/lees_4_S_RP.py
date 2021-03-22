import RPi.GPIO as GPIO
import time
#RP => LED4=GPIO12,LED3=GPIO16,LED2=GPIO20,LED1=GPIO21
S4=18
S3=23
S2=24
S1=25

S4_3_2_1={S4:"S4",S3:"S3",S2:"S2",S1:"S1"} 

GPIO.setmode(GPIO.BCM) # GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(S4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(S3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(S2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(S1,GPIO.IN, pull_up_down=GPIO.PUD_UP)


def read(schak_nr):
    status = GPIO.input(schak_nr)
    print(S4_3_2_1[schak_nr] , "=", status)
    time.sleep(0.5)

    
while 1:
    read(S4)
    read(S3)  
    read(S2)
    read(S1)
    print()


