import requests

my_headers = {"Accept":"application/json"}
response = requests.get("https://icanhazdadjoke.com/", timeout=5, headers=my_headers)


my_dict =response.json()

print(my_dict["joke"])