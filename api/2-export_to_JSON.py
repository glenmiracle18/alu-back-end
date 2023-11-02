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

    for todo in todos:
        break

    for user in users:
        if user.get("id") == user_id:
            name = user.get("username")

    data = [{
        user_id: [
            {
                'task': todo['title'],
                'completed': todo['completed'],
                'owner': name,
            }
        ]
    }]
    with open(file, 'w', newline='') as f:
        i = 0
        for i in user:
            
            json.dump(data, f)

        # for todo in todos:
        #     if todo.get("userId") == user_id:
        #         todo.update({"name": name})
        #         del todo["id"]
        #         writer.writerow(todo)
