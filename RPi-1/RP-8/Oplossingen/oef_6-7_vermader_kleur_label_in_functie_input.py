#Oef 6-7 Verander de kleur van een label van groen naar rood indien input van gesloten naar open verandert! 

from tkinter import *
import RPi.GPIO as GPIO
import time


window = Tk()
window.geometry("100x200")
window.title ("Toggle LED")

s1=18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_UP)


label_knop_status=Label(window, text=0 , bg = 'lightgreen' , font=('Times', '128'), relief = SUNKEN)
label_knop_status.place(x=5 , y =5)


while True:
    toestand_input = GPIO.input(s1)
    if  toestand_input== 1:
        label_knop_status["text"] = "1"
        label_knop_status["bg"] = "lightgreen"        
    else:
        label_knop_status["text"] = "0"
        label_knop_status["bg"] = "#0000ff" # rrggbb 00-ff
    print("loop still running")
    window.update()
