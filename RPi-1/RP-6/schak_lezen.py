from tkinter import *
import RPi.GPIO as GPIO

window = Tk()
window.title = "Schakelaar volgen"
window.geometry("800x400")

schakelaar =18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(schakelaar, GPIO.IN, pull_up_down=GPIO.PUD_UP)


mijnLabel1= Label( window, text = "S" ,relief =GROOVE)
mijnLabel1.place(x=10,y=50)


while True:
    toestand_nu = GPIO.input(schakelaar)
    mijnLabel1["text"]=toestand_nu
    window.update()
    