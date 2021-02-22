# betere oplossing via canvas widget tkinter

import tkinter as tk
from PIL import ImageTk, Image
import time

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("1220x800")
window.configure(background='yellow')

path = "pianoles.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
image =Image.open(path)
img = ImageTk.PhotoImage(image)
#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
my_foto_lbl = tk.Label(window, image = img)
my_foto_lbl.place(x=5,y=5)