import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()


mqtt_server = 'broker.mqttdashboard.com'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.0.172'
#mqtt_server = '192.168.1.144'

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'cvofocus/jenaam/esp_receive'
topic_pub = b'cvofocus/jenaam/esp_send'

last_message = 0
message_interval = 5
counter = 0

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
    
print('Connection WiFi successful')    
print('network config:', sta.ifconfig())




def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'notification' and msg == b'received':
        print('ESP received hello message')

def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print('Connected to %s MQTT broker, subscribed to topic >> %s ' % (mqtt_server, topic_sub.decode()))
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()
 
print("Program started!")

try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()

while True:
    try:
        client.check_msg()
        if (time.time() - last_message) > message_interval:
            msg = b'Hello #%d' % counter
            client.publish(topic_pub, msg)
            last_message = time.time()
            counter += 1
    except OSError as e:
        restart_and_reconnect()

