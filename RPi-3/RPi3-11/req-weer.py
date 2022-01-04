#https://api.openweathermap.org/data/2.5/weather?q=lokeren,be&units=metric&APPID=5b1d8efb4938ccfa55d1adaf6768dd08
import requests
import datetime

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=lokeren,be&units=metric&APPID=5b1d8efb4938ccfa55d1adaf6768dd08", timeout=5)

my_dict =response.json()
print("temp=",my_dict["main"]["temp"])
print("sunrise=",my_dict["sys"]["sunrise"])
print("sunset=",my_dict["sys"]["sunset"])
print("tijd=",my_dict["dt"])

sunrise_unix = my_dict["sys"]["sunrise"]
dt = datetime.datetime.fromtimestamp(sunrise_unix)
print(dt)

tijd_unix = my_dict["dt"]
dt = datetime.datetime.fromtimestamp(tijd_unix)
print(dt)



