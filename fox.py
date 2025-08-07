import requests
random_fox = requests.get('https://randomfox.ca/floof')
fox = random_fox.json()
fox1 = fox['image']
query_parameters = {"downloadformat": "jpg"}
response = requests.get(fox1, params = query_parameters)
with open('fox.jpg', 'wb') as file:
    file.write(response.content)