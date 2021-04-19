import tkinter


my_frame = tkinter.Frame(width = 50 , height = 25 , bg="yellow")
my_frame.place(x=0,y=0)

my_frame2= tkinter.Frame(width = 50 , height = 25 , bg="red")
my_frame2.place(x=0,y=100)


while 1:
    my_frame.update()

# oefening achterhaal wat er hier allemaal gebeurd :-)  waarom krijgen we iets te zien?
# wordt er een toplevel window gegenereerd? waar/wanneer
# is mainloop een methode van Frame?
