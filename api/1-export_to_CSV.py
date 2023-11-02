#!/usr/bin/python3
"""
getting data from the api
"""

import requests
import sys
import csv

if __name__ == "__main__":
    employee_Id = int(sys.argv[1])

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_data_url = "https://jsonplaceholder.typicode.com/users"

    user_response = requests.get(user_data_url)
    todo_response = requests.get(todo_url)

    # if todo_response.status_code & user_response.status_code == 200:
    todos = todo_response.json()
    users = user_response.json()

    order = ['userId', 'username', 'completed', 'title']

    for user in users:
        if user.get("id") == employee_Id:
            employee_name = user.get("username")

    with open(f'{employee_Id}.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=order, quoting=csv.QUOTE_ALL)

        for todo in todos:
            if todo.get("userId") == employee_Id:
                del todo['id']
                todo['username'] = user['username']
                writer.writerow(todo)
