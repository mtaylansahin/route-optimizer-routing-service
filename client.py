import requests

BASE = "http://localhost:8000/"
# BASE = "https://agile-bastion-03947.herokuapp.com/"

response = requests.post(BASE + 'greedy', json={'num_nodes':4, 'coordinates': [{'x':0, 'y':0}, {'x':1, 'y':1}, {'x':1, 'y':2}, {'x':2, 'y':2}]})
print(response.json())

response = requests.post(BASE + 'greedy', json={'num_nodes':5, 'coordinates': [{'x':0, 'y':0}, {'x':1, 'y':1}, {'x':1, 'y':2}, {'x':2, 'y':2}, {'x':2, 'y':1}]})
print(response.json())


response = requests.post(BASE + 'genetic', json={'num_nodes':4, 'coordinates': [{'x':0, 'y':0}, {'x':1, 'y':1}, {'x':1, 'y':2}, {'x':2, 'y':2}]})
print(response.json())

response = requests.post(BASE + 'genetic', json={'num_nodes':5, 'coordinates': [{'x':0, 'y':0}, {'x':1, 'y':1}, {'x':1, 'y':2}, {'x':2, 'y':2}, {'x':2, 'y':1}]})
print(response.json())
