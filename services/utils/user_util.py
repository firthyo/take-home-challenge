import json

def fetch_users():
    with open('../data/users.json', 'r') as file:
        users = json.load(file)
    return users

def save_users(users):
    with open('../data/users.json', 'w') as file:
        json.dump(users, file, indent=4)
