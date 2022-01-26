file_path = 'P10_FileAndEx\\guest.txt'

active = 'True'
while active == 'True':
    name_guest = input("Please enter your name: ")
    with open(file_path, 'a') as file_object:
        file_object.write(f"{name_guest}\n")
    confirm = input('Do you want add more people? (y/n): ')
    if confirm == 'n':
        break

with open(file_path, 'r') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(f"Hello {line.strip()}!")