from tkinter import *
import RPi.GPIO as GPIO


window = Tk()
window.geometry("250x50")
window.title ("Led on/off")

led=25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

def led_on():
    GPIO.output(led, GPIO.HIGH)

def led_off():
    GPIO.output(led, GPIO.LOW)


btn_on = Button(window, text="On", command=led_on)
btn_on.place(x=10, y=10)

btn_off = Button(window, text="Off", command=led_off)
btn_off.place(x=100, y=10)

window.mainloop()
