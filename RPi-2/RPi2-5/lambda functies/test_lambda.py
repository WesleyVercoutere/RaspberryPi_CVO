from tkinter import *

def button_pressed(p):
    print("p=", p)

def button_pressed_no_lambda(p="nothing"):
    print("nl p=", p)    

window = Tk()
window.geometry("600x500")  # not *
window.title("Control Stappenmotor")

'''

btn_goto_start = Button(window, text = "Start", width ="6" , command = lambda : button_pressed("start"))
btn_goto_start.place(x=10,y=100)

btn_goto_pos1 = Button(window, text = "Pos1", width ="6", command = lambda : button_pressed("pos1"))
btn_goto_pos1.place(x=100,y=100)

btn_goto_pos2 = Button(window, text = "Pos2", width ="6", command = lambda : button_pressed("pos2"))
btn_goto_pos2.place(x=200,y=100)

'''

btn_goto_start = Button(window, text = "Start", width ="6" , command = button_pressed_no_lambda)
btn_goto_start.place(x=10,y=100)

btn_goto_pos1 = Button(window, text = "Pos1", width ="6", command = button_pressed_no_lambda)
btn_goto_pos1.place(x=100,y=100)

btn_goto_pos2 = Button(window, text = "Pos2", width ="6", command = button_pressed_no_lambda )
btn_goto_pos2.place(x=200,y=100)

while 1:
    window.update()

