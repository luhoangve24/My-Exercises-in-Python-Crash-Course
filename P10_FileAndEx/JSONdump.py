import json

""" numbers = [2, 3, 5, 7, 9, 13]

file_name = 'numbers.json'
with open(file_name, 'w') as obj:
    json.dump(numbers, obj) """

file_path = 'numbers.json'
with open(file_path, 'r') as obj:
    numbers = json.load(obj)

print(numbers)