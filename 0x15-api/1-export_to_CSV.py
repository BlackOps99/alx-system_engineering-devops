#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{user_id}").json()
    username = user.get("username")
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows([
            {"userId": user_id, "username": username, "completed": t.get("completed"), "title": t.get("title")}
            for t in todos
        ])
