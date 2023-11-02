#!/usr/bin/python3
"""
getting data from the api
"""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_Id = int(sys.argv[1])

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_data_url = "https://jsonplaceholder.typicode.com/users"

    user_response = requests.get(user_data_url)
    todo_response = requests.get(todo_url)

    todos = todo_response.json()
    users = user_response.json()

    order = ['userId', 'username', 'completed', 'title']
    for user in users:
        if user.get("id") == employee_Id:
            employee_name = user.get("username")

    new = f"{employee_Id}.csv"
    with open(new, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=order, quoting=csv.QUOTE_ALL)
        for todo in todos:
            if todo.get("userId") == employee_Id:
                del todo['id']
                todo.update({'username': employee_name})
                writer.writerow(todo)
