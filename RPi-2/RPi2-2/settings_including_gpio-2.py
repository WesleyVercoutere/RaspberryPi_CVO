from tkinter import *
import json  # json.loads()  + json.dumps()  loads zet json om in dict en dumps zet dict om in json

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

schakelaars= [18,16,20]
GPIO.setup(schakelaars, GPIO.IN,pull_up_down=GPIO.PUD_UP)
leds=[23,24,25]
GPIO.setup(leds, GPIO.OUT)

status_led1 = False
status_led2 = False
status_led3 = False

#  vervang 3 onderstaande functies door 1

def callback_s1(p):
    global status_led1 , status_led2 ,status_led3 ,settings_obj
    if settings_obj["1"][0] == "1":
        print(">1")
        status_led1= not status_led1
        GPIO.output(leds[0], status_led1)
    if settings_obj["1"][1] == "1":
        print(type(settings_obj["1"][1]))
        print(">2")
        status_led2= not status_led2
        GPIO.output(leds[1], status_led2)
    if settings_obj["1"][2] == "1":
        print(">3")
        status_led3= not status_led3
        GPIO.output(leds[2], status_led3)        
    print("S1 pressed")

    
def callback_s2(p):
    global status_led1 , status_led2 ,status_led3 ,settings_obj
    if settings_obj["2"][0] == "1":
        print(">1")
        status_led1= not status_led1
        GPIO.output(leds[0], status_led1)
    if settings_obj["2"][1] == "1":
        print(type(settings_obj["1"][1]))
        print(">2")
        status_led2= not status_led2
        GPIO.output(leds[1], status_led2)
    if settings_obj["2"][2] == "1":
        print(">3")
        status_led3= not status_led3
        GPIO.output(leds[2], status_led3)        
    print("S2 pressed")
    
def callback_s3(p):
    global status_led1 , status_led2 ,status_led3 ,settings_obj
    if settings_obj["3"][0] == "1":
        print(">1")
        status_led1= not status_led1
        GPIO.output(leds[0], status_led1)
    if settings_obj["3"][1] == "1":
        print(type(settings_obj["1"][1]))
        print(">2")
        status_led2= not status_led2
        GPIO.output(leds[1], status_led2)
    if settings_obj["3"][2] == "1":
        print(">3")
        status_led3= not status_led3
        GPIO.output(leds[2], status_led3)        
    print("S3 pressed")
    
    
GPIO.add_event_detect(schakelaars[0], GPIO.FALLING, callback_s1, bouncetime=200)
GPIO.add_event_detect(schakelaars[1], GPIO.FALLING, callback_s2, bouncetime=200)
GPIO.add_event_detect(schakelaars[2], GPIO.FALLING, callback_s3, bouncetime=200)

window = Tk()
window.geometry("600x100")  # not *
window.title("LOAD AND SAVE SETTINGS")

current_settings=""
settings_obj = {}

def json_to_obj(par):
    global settings_obj
    settings_obj = json.loads(par)        
    string_var_setting_1.set(settings_obj["1"])
    string_var_setting_2.set(settings_obj["2"])
    string_var_setting_3.set(settings_obj["3"])
    
def check_create_default_settings():
    global current_settings

    default_settings = '{"1":"001","2":"010","3":"100"}'
    
    try:
        f = open("settings.txt","rt")
        print("File settings.txt exists!")
        current_settings = f.read()
        print("Settings are",current_settings)
        f.close()
        
        json_to_obj(current_settings) # convert json to dict en laadt in de entry fields

        
    except Exception as e:
        print("File settings.txt not exists, now we create it and save default settings!" , e)
        f = open("settings.txt","wt")
        f.write(default_settings)
        f.close()
        json_to_obj(default_settings) # convert json to dict en laadt in de entry fields
        print("File settings.txt made!")
        print("Settings are",default_settings)
    
    

def fct_btn_save():
    global settings_obj
    global current_settings  # format>> '{"1":"001","2":"010" , "3":"100"}'
    #current_settings = f'\{"1":{string_var_setting_1.get()},"2":{string_var_setting_2.get()},"3":{string_var_setting_3.get()}\}'
    #current_settings = f'{"1":{string_var_setting_1.get()},"2":{string_var_setting_2.get()},"3":{string_var_setting_3.get()}}'
    #current_settings = f'\u007b"1":"{string_var_setting_1.get()}","2":"{string_var_setting_2.get()}","3":"{string_var_setting_3.get()}"\u007d'
    # beter of makkelijker is :
    settings_obj["1"]=string_var_setting_1.get()
    settings_obj["2"]=string_var_setting_2.get()
    settings_obj["3"]=string_var_setting_3.get()
    
    current_settings = json.dumps(settings_obj)  # dictionary object to json text format with .dumps()
    print(type(current_settings))
    print("Saving current settings as>",current_settings)
    
    try:
        f = open("settings.txt","wt")
        f.write(current_settings)
        f.close
        print("Saved current settings as>",current_settings)
        
    except Exception as e:
        print("Error during saving >" ,e)
      
        
def fct_btn_load():
    # loads json from txt file and shows 3 values in the entry fields
    global settings_obj
    global current_settings  # format>> '{"1":"001","2":"010" , "3":"100"}'
    try:
        f = open("settings.txt","rt")
        current_settings = f.read()
        f.close()
        print("Loaded settings are",current_settings)
        
        json_to_obj(current_settings)   # convert json to dict en laadt in de entry fields
                                 
    except Exception as e:    
        print("Error loading settings >",e)

# button read and load settings
btn_save_settings = Button(window, text = "SAVE", command = fct_btn_save)
btn_save_settings.place(x=450,y=50)

btn_load_settings = Button(window, text = "LOAD", command = fct_btn_load)
btn_load_settings.place(x=525,y=50)

# labels text fields for settings S1,S2,S3
lbl_set_s1=Label(window, text = "Setting S1")
lbl_set_s1.place(x=10 , y = 10)

lbl_set_s2=Label(window, text = "Setting S2")
lbl_set_s2.place(x=160 , y = 10)

lbl_set_s3=Label(window, text = "Setting S3")
lbl_set_s3.place(x=310 , y = 10)

# entry text fields for settings S1,S2,S3

string_var_setting_1 = StringVar()  # string_var_setting_1.set("hello") en # string_var_setting_1.get() ipv #entry_set_s1.insert(0,"001")
string_var_setting_2 = StringVar()  
string_var_setting_3 = StringVar()

entry_set_s1 = Entry(window , width= 10 , textvariable= string_var_setting_1)
entry_set_s1.place(x=10 , y=50)


entry_set_s2 = Entry(window, width= 10 , textvariable= string_var_setting_2)
entry_set_s2.place(x=160 , y=50)


entry_set_s3 = Entry(window, width= 10 , textvariable= string_var_setting_3)
entry_set_s3.place(x=310 , y=50)


# main program
check_create_default_settings()
while True:
    window.update()




