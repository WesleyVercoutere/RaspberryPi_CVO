import RPi.GPIO as GPIO
import smbus

bus = smbus.SMBus(1)
addressPCF8574 = 0x38

bus.write_byte(addressPCF8574, 0xFF)# put all pins as inputs
    
while 1:
    status = bus.read_byte(addressPCF8574)
    status = status >> 4  #  shift right operator  dus alle bits 4 keer naar rechts 
    status = status | 0b11110000  # bit OR operator  OR met "1" geeft altijd "1"
    bus.write_byte(addressPCF8574, status)
    
    

