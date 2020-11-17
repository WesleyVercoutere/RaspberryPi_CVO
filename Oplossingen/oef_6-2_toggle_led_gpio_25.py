from tkinter import *
import RPi.GPIO as GPIO


window = Tk()
window.geometry("250x50")
window.title ("Toggle LED")

led=25
led2=23
status_led= 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

def led_toggle():
    global status_led
    status_led= not status_led
    GPIO.output(led, status_led)
    print("LED nu:",status_led)


btn_toggle = Button(window, text="TOGGLE LED", command=led_toggle)
btn_toggle.place(x=10, y=10)

window.mainloop()
