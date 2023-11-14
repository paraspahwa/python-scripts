# Consume a REST API using requests

import requests

api_url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(api_url)

if response.status_code == 200:
    todo_data = response.json()
    print("Title:", todo_data['title'])
    print("Completed:", todo_data['completed'])
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
