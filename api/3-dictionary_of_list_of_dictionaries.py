#!/usr/bin/python3
"""Export the TODO lists of all employees from a REST API to a JSON file."""
import json
import requests


API_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    users = requests.get("{}/users".format(API_URL)).json()
    todos = requests.get("{}/todos".format(API_URL)).json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        all_tasks[str(user_id)] = [{"username": user.get("username"),
                                    "task": todo.get("title"),
                                    "completed": todo.get("completed")}
                                   for todo in todos
                                   if todo.get("userId") == user_id]
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
