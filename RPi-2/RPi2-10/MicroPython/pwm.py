import machine
import time

uart1 = machine.UART(1, baudrate=9600, tx=33 , rx=32 )

#led = machine.Pin(23, machine.Pin.OUT)
#button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

pwm_out = machine.PWM(machine.Pin(23))
pwm_out.freq(1000)
pwm_value = 0

uart1.write("Hello from esp32!\n")

msg_b = b''

while True:
    if uart1.any() > 0:
        c = uart1.read(1)
        print("c=",c)
        if c == b'\n':
            if msg_b == b'up':
                if pwm_value < 923:
                    pwm_value +=100
                    
            else:
                if pwm_value > 100:
                    pwm_value -=100
                
            pwm_out.duty(pwm_value)
                
            msg_b=b'' # clear buffer
            
        elif c == b'\r':
            pass
        
        else:
            msg_b += c
            print("msg_b=",msg_b)

