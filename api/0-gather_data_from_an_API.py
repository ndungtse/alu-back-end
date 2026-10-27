#!/usr/bin/python3
"""Display the TODO list progress of an employee from a REST API."""
import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user = requests.get("{}/users/{}".format(API_URL, user_id)).json()
    todos = requests.get("{}/todos".format(API_URL),
                         params={"userId": user_id}).json()

    done = [todo for todo in todos if todo.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for todo in done:
        print("\t {}".format(todo.get("title")))
