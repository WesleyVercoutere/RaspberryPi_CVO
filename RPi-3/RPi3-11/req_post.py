import requests

mijn_data = "Requests biedt vele leuke mogelijkheden om te werken met API's"
response = requests.post("http://127.0.0.1:5555", timeout=5, data=mijn_data)

my_dict =response.json()
print(my_dict)

