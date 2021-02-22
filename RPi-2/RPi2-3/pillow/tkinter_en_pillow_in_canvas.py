from tkinter import *  
from PIL import ImageTk,Image

window = Tk()
window.title("Join")
window.geometry("1240x825")
window.configure(background='yellow')

canvas = Canvas(window, width = 1220, height = 805)  
canvas.pack()

img_pillow=Image.open("pianoles.jpg")
print(img_pillow.size)

img_tk = ImageTk.PhotoImage(img_pillow)

canvas.create_image(10, 10, anchor=NW, image=img_tk )

window.mainloop() 