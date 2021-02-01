# verkeerslicht
import RPi.GPIO as GPIO
import time

red=23
orange=24
green= 25

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(orange,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

print("Druk CTRL C om dit programma te beëindigen!")


while True:
    
    GPIO.output(red,0)
    GPIO.output(orange,0)
    GPIO.output(green,1)
    print("Verkeerslicht is nu groen!")        
    time.sleep(4)
    
    GPIO.output(red,0)
    GPIO.output(orange,1)
    GPIO.output(green,0)
    print("Verkeerslicht is nu oranje!")        
    time.sleep(4)
    
    GPIO.output(red,1)
    GPIO.output(orange,0)
    GPIO.output(green,0)
    print("Verkeerslicht is nu rood!")        
    time.sleep(4)
    

