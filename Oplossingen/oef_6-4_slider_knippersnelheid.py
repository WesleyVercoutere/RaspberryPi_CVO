from tkinter import *
import RPi.GPIO as GPIO
import time


window = Tk()
window.geometry("250x100")
window.title ("Toggle LED")

led=25
status_led= 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

def led_toggle():
    global status_led
    status_led= not status_led
    GPIO.output(led, status_led)
    print("LED nu:",status_led)

def change_slider(p):
    global knippersnelheid
    knippersnelheid=int(p)
    print("p=",p)
        
slider = Scale(window, from_=1,to=10, tickinterval =1 , length= 200, orient = HORIZONTAL , command = change_slider)
slider.place(x=10, y=10)

time_vorige=0
knippersnelheid=1

while True:    
    if time.time() - time_vorige > (1/knippersnelheid)/2:        
        led_toggle()
        time_vorige=time.time()      
    print("test in while")
    window.update()
