import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # nummering volgens GPIO's
GPIO.setwarnings(False) # disabelt de waarschuwingen

ga_naar_start_button = 13
ga_naar_pos1_button = 6
ga_naar_pos2_button =  5

inputs = (ga_naar_start_button, ga_naar_pos1_button, ga_naar_pos2_button)
GPIO.setup(inputs, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttons(p="nothing"):
    print("buttons p=", p)

'''

GPIO.add_event_detect(ga_naar_start_button, GPIO.FALLING, callback=lambda a: buttons(ga_naar_start_button), bouncetime=200)
GPIO.add_event_detect(ga_naar_pos1_button, GPIO.FALLING, callback=lambda a: buttons(ga_naar_pos1_button), bouncetime=200)
GPIO.add_event_detect(ga_naar_pos2_button, GPIO.FALLING, callback=lambda a: buttons(ga_naar_pos2_button), bouncetime=200)

'''


GPIO.add_event_detect(ga_naar_start_button, GPIO.FALLING, callback=buttons, bouncetime=200)
GPIO.add_event_detect(ga_naar_pos1_button, GPIO.FALLING, callback=buttons, bouncetime=200)
GPIO.add_event_detect(ga_naar_pos2_button, GPIO.FALLING,callback=buttons, bouncetime=200)

while 1:
    pass