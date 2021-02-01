# deze Oef is gecopierd van Wesly en aangepast voor pigpio
from tkinter import Tk,Label
import pigpio
import RPi.GPIO as GPIO


# GPIO general
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pinRotBtn = 21
inputs = (pinRotBtn)    #  ,pinRotA,pinRotB)  worden door rotary encoder geïnitialiseerd in PUD_DOWN    pinPushBtn, ???
GPIO.setup(inputs,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

my_pi=pigpio.pi()

pinRotA =  20
pinRotB = 16  
my_pi.set_mode(pinRotA , pigpio.INPUT)
my_pi.set_mode(pinRotB , pigpio.INPUT)
my_pi.set_pull_up_down(pinRotA, pigpio.PUD_DOWN)
my_pi.set_pull_up_down(pinRotB, pigpio.PUD_DOWN)

teller=0

def cbf(p1,p2,p3):
    global teller
    print(p1,p2,p3)
    if (my_pi.read(pinRotB)):
        teller+=1
    else:
        teller-=1        
    print(teller)
    
my_pi.callback(pinRotA, pigpio.FALLING_EDGE, cbf)

while 1:
    pass

