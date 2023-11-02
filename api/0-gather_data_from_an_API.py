#!/usr/bin/python3

"""project finale"""
import sys
import requests

employee_Id = sys.argv[2]

api_url = "https://jsonplaceholder.typicode.com/todos?userID={employee_id}"
user_data_url = "https://jsonplaceholder.typicode.com/users"

user_response = requests.get(user_data_url)
response = requests.get(api_url)

if response.status_code & user_response.status_code == 200:
    todos = response.json
    users = user_response.json

    # filter completed tasks
    completed_tasks = []
    todo_items = []
    for todo in todos():
        if employee_Id == todo['userId']:
            todo_items.append(todo)
            if todo['completed'] is True:
                completed_tasks.append(todo)

    # get the employee name
    for user in users():
        if user['id'] == employee_Id:
            employee_name = user['name']

    # Display the progress information
    print(f"Employee {employee_name} is done with \
    tasks({len(completed_tasks)}/{len(todo_items)}): ")
    for task in completed_tasks:
        print(f"/t{task['title']}")
    else:
        print(f"Error: {response.status_code}")
