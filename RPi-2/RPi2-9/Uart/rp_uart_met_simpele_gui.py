import serial
import time
from tkinter import *

c = 0
msg = b""
msgstr = ""

port = serial.Serial("/dev/ttyS0",9600)

send = "Hello from RPi!"
send = send.encode()
port.write(send)

def fct_send_message(message):
    port.write(message.encode())

window = Tk()
window.geometry("300x150")

btn_Blue = Button(window, text = "on", font = "bold", width = 2,fg = "blue", command = lambda: fct_send_message("on"))
btn_Blue.place(x = 50, y = 25)

btn_Red = Button(window, text = "off", font = "bold", width = 2,fg = "red", command = lambda:fct_send_message("off"))
btn_Red.place(x = 50, y = 75)


while 1:
    window.update()
    if port.inWaiting() > 0:
        c = port.read()        
        if c==b'\n':
            #print("message=",msg)
            msgstr=msg.decode()
            print(">",msgstr)               
            msg=b""
            msgstr=""
        else:
            msg += c  
