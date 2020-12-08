import RPi.GPIO as GPIO
import time
from gpiozero import MCP3008

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
red = 23
GPIO.setup(red, GPIO.OUT)

mcp3008_channel_0 = MCP3008(channel=0, device=0)
p = GPIO.PWM(red, 50)  # channel=23 frequency=50Hz
p.start(0)  # dc=0

while True:
    potmeter = int(mcp3008_channel_0.value *100)
    print(potmeter) 
    p.ChangeDutyCycle(potmeter)
    time.sleep(0.250)
