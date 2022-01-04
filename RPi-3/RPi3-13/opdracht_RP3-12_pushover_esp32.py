import urequests as requests
import network
import ujson as json
import esp
import machine
import time
# Set the debug to None and activate the garbage collector.
esp.osdebug(None)
import gc
gc.collect()

ssid = 'telenet-54336'
password = 'hwwmbxrswM'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

##################################################
service_button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
service_button_status_vorige =1
##################################################
##################################################
panic_button = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
panic_button_status_vorige =1
##################################################
last_message = 0
message_interval = 60
counter = 0

while station.isconnected() == False:
  pass

print('Connection  now successful')
print(station.ifconfig())
############################################

print("Started panic alarm system")


try:
    while True:
        panic_button_status = panic_button.value()
        if panic_button_status !=  panic_button_status_vorige:
            panic_button_vorige = panic_button_status
            if panic_button_status == 0 :
                print("start sending..")
                url = 'http://api.pushover.net/1/messages.json'
                data_to_send = "token=ahbf2c758j9xe2qgxhrs7z8aip6r&user=umpvs3iq2dvci87nkn7axg1ubtgk&title=wim lokeren&message=panic-alarm&priority=2&retry=30&expire=60&sound=persistent"
                x = requests.post(url, data = data_to_send, headers = {"Content-Type": "application/x-www-form-urlencoded"})
                print(x.text)
                if "status=1" in x.text:
                    print("Panic message sended to Pushover server!")
                else:
                    print("Panic message not succesfully sended to Pushover server!")                    

            time.sleep(0.2)
            
        service_button_status = service_button.value()
        if service_button_status !=  service_button_status_vorige:
            service_button_status_vorige = service_button_status
            if service_button_status == 0 :
                print("start sending..")
                url = 'http://api.pushover.net/1/messages.json'
                data_to_send = "token=ahbf2c758j9xe2qgxhrs7z8aip6r&user=umpvs3iq2dvci87nkn7axg1ubtgk&title=wim lokeren&message=panic-alarm&priority=2&retry=30&expire=30&sound=pianobar"
                x = requests.post(url, data = data_to_send, headers = {"Content-Type": "application/x-www-form-urlencoded"})
                print(x.text)
                if "status=1" in x.text:
                    print("Service message sended to Pushover server!")
                else:
                    print("Service message not succesfully sended to Pushover server!")                    

            time.sleep(0.2)
            
except Exception as e:
    print("e=",e)
    
finally:
    print("finally")






