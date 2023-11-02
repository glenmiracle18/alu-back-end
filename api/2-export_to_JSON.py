#!/usr/bin/python3
"""
gathing data from an api
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])

    file = f"{user_id}.json"

    r1 = requests.get("https://jsonplaceholder.typicode.com/users")

    users = r1.json()

    r2 = requests.get("https://jsonplaceholder.typicode.com/todos")

    todos = r2.json()

    for user in users:
        if user.get("id") == user_id:
            name = user.get("username")

    todo_data = []
    for todo in todos:
        if todo.get("userId") == user_id:
            todo_data.append(
                    {
                        'task': todo['title'],
                        'completed': todo['completed'],
                        'owner': name,
                    })
    print(todo_data)

    user_data = {
        user_id: todo_data
    }

    with open(file, 'w', newline='') as f:
        json.dump(user_data, f)
