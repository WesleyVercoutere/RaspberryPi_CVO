# Configure the ESP32 wifi as Station mode.
from machine import Pin
import network
import sys
ssid = "telenet-5432836";
password = "hwwmbxr7sswM";

sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
  print('connecting to network...')
  sta.active(True)
  #sta.connect('your wifi ssid', 'your wifi password')
  sta.connect(ssid, password)
  while not sta.isconnected():
    pass
print('network config:', sta.ifconfig())

# ************************
# Configure the socket connection over TCP/IP
import socket
PORT=8080
# AF_INET - use Internet Protocol v4 addresses
# SOCK_STREAM means that it is a TCP socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',PORT)) # specifies that the socket is reachable by any address the machine happens to have
s.listen(5)     # max of 5 socket connections


led=Pin(2, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_UP)

def find_name_and_type(request):
    STARTPAGE = "index_uit.html"
    lines = request.split("\n")
    first_line = lines[0]
    print(first_line)

    pos_forward_slash = first_line.index("/")  # -1 if not found
    if pos_forward_slash >=0:
        pos_http = first_line.index("HTTP")
        name_and_type = first_line[pos_forward_slash + 1 : pos_http-1]
        if name_and_type == "":
            name_and_type = STARTPAGE
        print("name_and_type=",name_and_type)
        pos_dot = name_and_type.index(".")
        type_file = name_and_type[pos_dot +1:]
    return name_and_type, type_file
        
    
    

def antwoord_browser(bestands_naam, type_bestand):
    #print(">>bestands_naam=",bestands_naam,"type_bestand=",type_bestand)
    try:
        if type_bestand == "html" or type_bestand == "txt" or type_bestand == "css":
            f = open(bestands_naam,"r") # default "rt" not needed to specify   b for binary ...
        elif type_bestand == "cmd":
            pass
        else:
            f = open(bestands_naam,"rb") # default "rt" not needed to specify   b for binary ...
            
        if type_bestand == "cmd":
            if "on" in bestands_naam:
                response = "server ontving " + bestands_naam
                led.value(1)
            elif "off" in bestands_naam:
                response = "server ontving " + bestands_naam
                led.value(0)
            elif "get" in bestands_naam:
                stat = button.value()
                print("stat=",stat)
                if stat == 1:
                    response = "off"
                else:
                    response = "on"
        else:
            response = f.read()
            f.close()
            
        length_response = len(response)
        print("\nDe respons heeft een lengte=", length_response, "bytes")
        
        conn.sendall(b"HTTP/1.1 200 OK\r\n")
        
        if not type_bestand!="html" and  not type_bestand!="cmd":
            conn.sendall(b"Cache-Control: max-age=3600\r\n")
             
        if type_bestand=="gz.css" or type_bestand=="gz.js":
             conn.sendall(b"Content-encoding: gzip\r\n") 
        
        if type_bestand=="html":
            conn.sendall(b"Content-Type: text/html\r\n")
        elif type_bestand=="cmd":
            conn.sendall(b"Content-Type: text/html\r\n")        
        elif type_bestand=="jpg":
            conn.sendall(b"Content-Type: imgage/jpg\r\n")
        elif type_bestand=="png":
            conn.sendall(b"Content-Type: image/png\r\n")
        elif type_bestand=="ico":
            conn.sendall(b"Content-Type: image/ico\r\n")
        elif type_bestand=="css" or type_bestand=="gz.css":
            conn.sendall(b"Content-Type: text/css\r\n")
        elif type_bestand=="js" or type_bestand=="gz.js":
            conn.sendall(b"Content-Type: text/javascript\r\n")            
        else:
            print("no type found!")
            
        content_length_header="Content-Length:"+str(length_response)+"\r\n\r\n"
        conn.sendall(content_length_header.encode("UTF-8"))  # we beginnen te tellen NA de lege lijn!
        
            
        if type_bestand=="html" or type_bestand == "txt" or type_bestand == "cmd":
            conn.sendall(response.encode("UTF-8")) # zet string om naar bytes
        else:
            conn.sendall(response) # 
        conn.close()
        
    except Exception as e:

        print("Except in antwoord_browser !!", e)
        conn.close()      

try:
    while True:
        print("Server is waiting for a connection on port", PORT)
        conn, addr = s.accept()
        print('Server got a connection from' , addr)
        
        request = (conn.recv(4096)).decode("UTF-8")
        print("len request =",len(request))
        print("message from client=",request)
        
        if len(request) > 0:             
            full_name, type_file = find_name_and_type(request)
            print("name_file =", full_name,  "type_file =", type_file)
            antwoord_browser(full_name, type_file)
            print("\nServer closed connection!**************************************************\n")

except Exception as e:
    print("Except in main!!", e)

