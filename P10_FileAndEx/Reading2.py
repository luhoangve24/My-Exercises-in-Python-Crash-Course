file_path = 'E:\\Lab\\GitHub\\pcc_2e\\chapter_10\\pi_million_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

my_birthday = input("Enter your birthday in the form ddmmyy: ")
if my_birthday in pi_string:
    print("Sure!")
else:
    print("Poor!")