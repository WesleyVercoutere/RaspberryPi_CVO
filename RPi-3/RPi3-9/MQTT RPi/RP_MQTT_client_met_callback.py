#Python MQTT client RP  met callback
# sudo pip install paho-mqtt
import paho.mqtt.client as mqtt #import the client1
import time
import sys

import RPi.GPIO as GPIO

#drukknop=18
drukknop=12
led_toggle =23
led_follow=24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(drukknop,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_toggle,GPIO.OUT)
GPIO.setup(led_follow,GPIO.OUT)


def fct_drukknop_falling(par):
    print("knop ingedrukt",par)
    client.publish("cvofocus/wimverlinden/msg_for_esp", "drukknop RP ingedrukt "+str(teller) )

GPIO.add_event_detect(drukknop,GPIO.FALLING, callback=fct_drukknop_falling, bouncetime=200)


def mqtt_message_arrived(client , userdata, msg):
    print("topic =" , msg.topic , "payload =" , msg.payload.decode())

client = mqtt.Client() #create new instance
client.on_message = mqtt_message_arrived

if client.connect("broker.mqttdashboard.com",1883, 60) !=0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.subscribe("cvofocus/wimverlinden/msg_from_esp")

print("Verbonden met de broker")

toestand_drukknop_daarnet=1
teller=0

try:
    print("Druk op CTRL+C om te eindigen")
    while True:
        client.loop_start()

except:
    client.loop_stop()
    print("Verbinding met broker verbreken")
    
client.disconnect()
print("Verbinding verbroken")  