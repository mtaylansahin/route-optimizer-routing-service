import requests

BASE = "http://localhost:5000/"

response = requests.get(BASE + 'helloworld/testname/20')

print(response.json())