# step 2 koppel aan txt bestand
from tkinter import *
import json  # json.loads()  + json.dumps()  loads zet json om in dict en dumps zet dict om in json

window = Tk()
window.geometry("600x100")  # not *
window.title("LOAD AND SAVE SETTINGS")

current_settings=""
settings_obj = {}

def check_create_default_settings():
    global current_settings
    default_settings = '{"1":"001","2":"010" , "3":"100"}'
    try:
        f = open("settings.txt","rt")
        print("File settings.txt exists!")
        current_settings = f.read()
        print("Settings are",current_settings)
        f.close()
    except FileNotFoundError:
        print("File settings.txt not exists, now we create it and save default settings!")
        f = open("settings.txt","wt")
        f.write(default_settings)
        f.close()
        print("File settings.txt made!")
        print("Settings are",default_settings)
        current_settings=default_settings
    
    

def fct_btn_save():
    global current_settings  # format>> '{"1":"001","2":"010" , "3":"100"}'
    #current_settings = f'\{"1":{string_var_setting_1.get()},"2":{string_var_setting_2.get()},"3":{string_var_setting_3.get()}\}'
    #current_settings = f'{"1":{string_var_setting_1.get()},"2":{string_var_setting_2.get()},"3":{string_var_setting_3.get()}}'
    #current_settings = f'\u007b"1":"{string_var_setting_1.get()}","2":"{string_var_setting_2.get()}","3":"{string_var_setting_3.get()}"\u007d'
    # beter of makkelijker is :
    settings_obj["1"]=string_var_setting_1.get()
    settings_obj["2"]=string_var_setting_2.get()
    settings_obj["3"]=string_var_setting_3.get()
    
    current_settings = json.dumps(settings_obj)
    print(type(current_settings))
    print("Saving current settings as>",current_settings)
    
    try:
        f = open("settings.txt","wt")
        f.write(current_settings)
        f.close
        print("Saved current settings as>",current_settings)
    except FileNotFoundError:
        print("Error during saving")
      
        
def fct_btn_load():
    # loads json from txt file and shows 3 values in the entry fields
    global settings_obj
    global current_settings  # format>> '{"1":"001","2":"010" , "3":"100"}'
    try:
        f = open("settings.txt","rt")
        current_settings = f.read()
        f.close()
        print("Settings are",current_settings)
        
        settings_obj = json.loads(current_settings)
        string_var_setting_1.set(settings_obj["1"])
        string_var_setting_2.set(settings_obj["2"])
        string_var_setting_3.set(settings_obj["3"])
                                 
    except FileNotFoundError:    
        print("Error loading settings!")

# button read and load settings
btn_save_settings = Button(window, text = "SAVE", command = fct_btn_save)
btn_save_settings.place(x=450,y=50)

btn_load_settings = Button(window, text = "LOAD", command = fct_btn_load)
btn_load_settings.place(x=500,y=50)

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

entry_set_s1 = Entry(window , width= 20 , textvariable= string_var_setting_1)
entry_set_s1.place(x=10 , y=50)
#string_var_setting_1.set("001") 

entry_set_s2 = Entry(window, width= 20 , textvariable= string_var_setting_2)
entry_set_s2.place(x=160 , y=50)
#string_var_setting_2.set("010")

entry_set_s3 = Entry(window, width= 20 , textvariable= string_var_setting_3)
entry_set_s3.place(x=310 , y=50)
#string_var_setting_3.set("100")

# main program
check_create_default_settings()
while True:
    window.update()

