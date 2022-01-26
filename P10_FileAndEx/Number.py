try:
    number = input("Please input a number: ")
    number = int(number)
except ValueError:
    print("Please! It isn't a number!?")
else:
    print(f"Your number: {number}")
