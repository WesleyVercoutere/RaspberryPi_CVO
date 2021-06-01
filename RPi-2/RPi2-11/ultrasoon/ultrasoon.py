import time

import machine

trigger = machine.Pin(23, machine.Pin.OUT)

while True:
    
    trigger.on()
    time.sleep(0.000010)   # minimum 10us , will be more because switching pins takes 7us     
    trigger.off()
    
    time.sleep(0.1)  # wait more then 60ms before sending a new pulse     
    
    
'''
oefening 1

print de correcte afstand in cm

oefenig 2

check of de waarde correct is :
echo 0 wanneer puls gegeven wordt?
echo puls niet te lang?

oefening 3

kan dit met interrupts zodat je enkel de trigger pulse moet geven?

'''

