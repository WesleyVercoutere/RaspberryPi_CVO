from tkinter import *
import RPi.GPIO as GPIO
import time


window = Tk()
window.geometry("500x200")
window.title ("Toggle LED")

led=25
tijd_aan=1
status_led =0
time_start=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

def led_aan():
    global status_led, time_start
    time_start=time.time()
    status_led = 1
    GPIO.output(led, 1)
    print("LED nu aan!")


def change_slider(p):
    global tijd_aan
    tijd_aan=int(p)
    print("tijd_aan=",tijd_aan)
        
btn_toggle = Button(window, text="LICHT AAN", command=led_aan)
btn_toggle.place(x=10, y=10)

slider = Scale(window, from_=1,to=100, tickinterval =10 , length= 450, orient = HORIZONTAL , command = change_slider)
slider.place(x=10, y=50)

time_vorige=0
knippersnelheid=1

while True:
    if (time.time() - time_start >= tijd_aan) :        
            GPIO.output(led, 0)
            print("LED nu uit!")
            #status_led = 0
    #print("loop still running")
    window.update()
