from tkinter import *
import RPi.GPIO as GPIO


window = Tk()
window.geometry("250x50")
window.title ("Toggle LED")

led=25
status_led= 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

def led_toggle(p):
    global status_led
    status_led= not status_led
    GPIO.output(led, status_led)
    txt_led_status["text"] = status_led
    print("LED nu:",status_led)


btn_toggle = Button(window, text="TOGGLE LED", command=led_toggle)
btn_toggle.place(x=10, y=10)

txt_led_status = Label(window, text="0" , relief = "sunk")
txt_led_status.place(x=150 , y = 15)

window.mainloop()
