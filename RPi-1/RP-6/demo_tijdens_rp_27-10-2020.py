from tkinter import *

window = Tk()
window.geometry("800x400")  # not *
window.title("CVOFOCUS")

mijn_label1=Label( window, text = "Level=40" ,relief =GROOVE)
mijn_label1.place(x=10,y=50)

my_entry= Entry(window)
my_entry.place(x=10, y=75)

my_entry2= Entry(window)
my_entry2.place(x=200, y=75)

def fct_aan():
    print("hi van fct_aan")
    mijn_label1["text"]="op mijn button gedrukt"

mijnButton= Button(window, text = "AAN" , width = 15 , height = 1 , command= fct_aan )
mijnButton.place(x=10, y=125)

def fct_kleur():
    mijn_label1["fg"]="red"    

mijnButton2= Button(window, text = "rood" , width = 15 , height = 1 , command= fct_kleur )
mijnButton2.place(x=10, y=175)


def fct_kleur_button():
    mijnButton["fg"]="blue"    

mijnButton3= Button(window, text = "blauw" , width = 15 , height = 1 , command= fct_kleur_button )
mijnButton3.place(x=10, y=225)

def fct_scale1(p):
    print("hi van fct_scale1",p)    

mijnSlider1 = Scale(window, from_=20, to=50,  tickinterval=10, orient=HORIZONTAL, command = fct_scale1 )
mijnSlider1.place(x=10, y=275)


#•   mijnTekstvak1.insert(0,"default tekst")

def fct_insert():
    my_entry.delete(0, "end")
    my_entry.insert(0,"Lukt het?")
   

mijnButton4= Button(window, text = "voeg in" , width = 15 , height = 1 , command= fct_insert )
mijnButton4.place(x=10, y=350)

def fct_tr():
    varx=my_entry.get()
    my_entry2.delete(0, "end")
    my_entry2.insert(0,varx)
    fct_opslaan(varx)

   
mijnButton5= Button(window, text = "transfer" , width = 15 , height = 1 , command= fct_tr )
mijnButton5.place(x=200, y=150)