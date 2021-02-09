#json

import json

default_settings = '{"1":"001","2":"010" , "3":"100"}'  # JSON FORMAT

json_to_obj = json.loads(default_settings) # loads method  makes from the json string a dictionary object

print(json_to_obj["1"]) # check value with key 1

print(json_to_obj["2"])

print(json_to_obj["3"])

json_to_obj["1"] = "110" # change value with key 1

json_to_obj["2"] = "011"

json_to_obj["3"] = "101"

print(json_to_obj)  # prints a dicitonary

new_settings_in_json_format = json.dumps(json_to_obj) # dumps method changes dictionary object to a string

print("new_settings_in_json_format=",new_settings_in_json_format)