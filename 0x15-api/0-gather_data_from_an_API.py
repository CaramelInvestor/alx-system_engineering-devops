#!/usr/bin/env python3
"""This module contains functions for gathering data from an API"""


from sys import argv
from requests import get

# rest api url
API = "https://jsonplaceholder.typicode.com"


# Functions required to process the API data
def get_user(user_id):
    """Get user by id"""
    return get(f"{API}/users/{user_id}").json()


def get_todos_of_user(user):
    """Get user's todos"""
    todos = get(f"{API}/todos").json()
    todos_of_user = [todo for todo in todos if todo["userId"] == user["id"]]
    return todos_of_user


def get_todos_done_by_user(user, todos):
    """Get user's done todos"""
    return [todo for todo in todos if todo["userId"] == user["id"]
            and todo["completed"]]


if __name__ == "__main__":
    if len(argv) < 1:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    else:
        user = get_user(argv[1])
        todos = get_todos_of_user(user)
        todos_done = get_todos_done_by_user(user, todos)

        print(
            f"Employee {user['name']} is done with tasks ({len(todos_done)}/{len(todos)}):")
        for done in todos_done:
            print("\t {}".format(done["title"]))
