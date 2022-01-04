import threading
import time

def webserver(par =""):
    print("de ontvangen parameter in de functie webserver=",par)
    while True:
        time.sleep(2)
        print("webserver thread")
    
def websocketserver(par=""):
    print("de ontvangen parameter in de functie websocketserver=",par)
    while True:
        time.sleep(3)
        print("websocketserver thread")
    
t1= threading.Thread(target= webserver, daemon=True)
t2= threading.Thread(target= websocketserver, daemon=True)    

#t1= threading.Thread(target= webserver, daemon=False)
#t2= threading.Thread(target= websocketserver, daemon=False)

t1.start()
print("t1 started")
t2.start()
print("t2 started")

print("threading.active_count()",threading.active_count())

#t1.join()
#t2.join()

print("end")