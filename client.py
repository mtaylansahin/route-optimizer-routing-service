import requests

BASE = "http://localhost:5000/"

response = requests.put(BASE + 'video/1', {'name':'first video', 'views':20, 'like':5})
print(response.json())

response = requests.get(BASE + 'video/1')
print(response.json())

response = requests.delete(BASE + 'video/1')
print(response)

response = requests.get(BASE + 'video/1')
print(response.json())