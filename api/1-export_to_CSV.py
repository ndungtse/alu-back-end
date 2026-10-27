#!/usr/bin/python3
"""Export the TODO list of an employee from a REST API to a CSV file."""
import csv
import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user = requests.get("{}/users/{}".format(API_URL, user_id)).json()
    todos = requests.get("{}/todos".format(API_URL),
                         params={"userId": user_id}).json()

    username = user.get("username")
    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, username,
                             todo.get("completed"), todo.get("title")])
