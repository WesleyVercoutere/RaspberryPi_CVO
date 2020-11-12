import tkinter as tk
from PIL import ImageTk, Image
import time

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("500x500")
window.configure(background='grey')

path = "wim_s.jpg"
x=50
y=50

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
image =Image.open(path)
img = image.resize((50, 50), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
#img = img.resize((50, 50), Image.ANTIALIAS)
#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
my_foto_lbl = tk.Label(window, image = img)
my_foto_lbl.place(x=5,y=5)

#The Pack geometry manager packs widgets in rows or columns.
#panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
while True:
    for x in range (50,480,10):
        img = image.resize((x, x), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        my_foto_lbl["image"]=img
        window.update()
    time.sleep(1)        
    for x in range (470,40,-10):
        img = image.resize((x, x), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        my_foto_lbl["image"]=img
        window.update()    
    time.sleep(1)
     
     

