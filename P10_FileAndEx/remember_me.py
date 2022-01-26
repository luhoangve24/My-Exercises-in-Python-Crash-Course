import json
from msilib.schema import File
from os import name

def get_stored_username(file_path):
    '''Get stored user name if available'''
    try:
        with open(file_path, 'r') as obj:
            name = json.load(obj)
    except FileNotFoundError:
        return None
    else:
        return name

def create_new_username(file_path):
    '''Get username from user'''
    name = input("Please enter your username: ")
    with open(file_path, 'w') as obj:
        json.dump(name, obj)
    print(f"We'll remember your username for next comeback, {name}!")

def greeting_user(file_path):
    if get_stored_username(file_path):
        name = get_stored_username(file_path)
        print(f"Hello {name}!")
    else:
        create_new_username(file_path)