import tkinter as tk

window = tk.Tk()
window.geometry("500x200")
window.title("TEST Button")

mijn_knop1 = tk.Button(window, text="klik hier" ,width=15)
mijn_knop1.place(x=5,y=5)

toggle_button2=False

def fct_button2():
    global toggle_button2
    toggle_button2 = not toggle_button2
    print("Knop 2 werd ingedrukt")
    if toggle_button2:
          mijn_knop2["bg"]="green"              
    else:
         mijn_knop2["bg"]="red" 

mijn_knop2 = tk.Button(window, text="klik hier 2", command = fct_button2 ,width=15)
mijn_knop2.place(x=5,y=50)

toggle_button3=False

def fct_button3():
    global mijn_knop3,mijn_image ,toggle_button3
    toggle_button3= not toggle_button3
    print("Knop 3 werd ingedrukt",toggle_button3)
    if toggle_button3:
        mijn_image=tk.PhotoImage(file="on.gif")       
    else:
        mijn_image=tk.PhotoImage(file="off.gif")             
    #mijn_knop3.configure(image=mijn_image)
    mijn_knop3["image"]=mijn_image    
    


mijn_image=tk.PhotoImage(file="off.gif")
mijn_knop3 = tk.Button(window,  image = mijn_image, command = fct_button3 )
mijn_knop3.place(x=150,y=5)

while True:
    window.update()