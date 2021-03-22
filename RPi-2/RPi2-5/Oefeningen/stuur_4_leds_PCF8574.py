import smbus
import time
 
LED5 = 0b11111110
LED6 = 0b11111101
LED7 = 0b11111011
LED8 = 0b11110111

bus = smbus.SMBus(1)

addressPCF8574 = 0x38

def led_on_500ms(led_nr):
    bus.write_byte(addressPCF8574, led_nr)    
    time.sleep(0.5)
    bus.write_byte(addressPCF8574, led_nr)      
    
while True:
    led_on_500ms(LED5)
    led_on_500ms(LED6)    
    led_on_500ms(LED7)    
    led_on_500ms(LED8)
    
    