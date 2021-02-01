#Oef 6-8 toon een open of gesloten schakelaar in je GUI die de toestand van je schakelaar aan een pin volgt.

from tkinter import *
import RPi.GPIO as GPIO
import time


window = Tk()
window.geometry("350x75")
window.title ("Toggle LED")

s1=18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

gif_s_open =PhotoImage(file="open.gif")
gif_s_closed =PhotoImage(file="closed.gif")

label_knop_status=Label(window, image= gif_s_closed, relief = SUNKEN)
label_knop_status.place(x=5 , y =5)


while True:
    toestand_input = GPIO.input(s1)
    if  toestand_input== 1:
        label_knop_status["image"] = gif_s_closed
    else:
        label_knop_status["image"] = gif_s_open
    print("loop still running")
    window.update()
