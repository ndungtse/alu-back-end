#!/usr/bin/python3
"""Export the TODO list of an employee from a REST API to a JSON file."""
import json
import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user = requests.get("{}/users/{}".format(API_URL, user_id)).json()
    todos = requests.get("{}/todos".format(API_URL),
                         params={"userId": user_id}).json()

    username = user.get("username")
    tasks = [{"task": todo.get("title"),
              "completed": todo.get("completed"),
              "username": username} for todo in todos]
    with open("{}.json".format(user_id), "w") as json_file:
        json.dump({str(user_id): tasks}, json_file)
