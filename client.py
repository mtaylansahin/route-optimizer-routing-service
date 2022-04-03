import requests

BASE = "http://localhost:8000/"

response = requests.post(BASE + 'greedy', json={'num_nodes':5, 'distances': [[0], [1, 0], [3, 2, 0], [5, 1, 4, 0], [9, 12, 21, 3, 0]]})
print(response.json())

response = requests.post(BASE + 'genetic', json={'num_nodes':5, 'distances': [[0], [1, 0], [3, 2, 0], [5, 1, 4, 0], [9, 12, 21, 3, 0]]})
print(response.json())
