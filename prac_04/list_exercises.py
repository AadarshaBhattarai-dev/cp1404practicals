"""
CP1404/CP5632 Practical 04
"""

def number_summary():
    #Ask the user for 5 numbers and print first, last, smallest, largest and average.
    numbers = []
    for i in range(1, 6):
        value = float(input("Number: "))
        numbers.append(value)

    first = numbers[0]
    last = numbers[-1]
    smallest = min(numbers)
    largest = max(numbers)
    average = sum(numbers) / len(numbers)

    def nice_print(num):
        return int(num) if num.is_integer() else num

    print(f"The first number is {nice_print(first)}")
    print(f"The last number is {nice_print(last)}")
    print(f"The smallest number is {nice_print(smallest)}")
    print(f"The largest number is {nice_print(largest)}")
    print(f"The average of the numbers is {average}")

def username_check():
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
        'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
        'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
    ]
    user = input("Enter your username: ")
    if user in usernames:
        print("Access granted")
    else:
        print("Access denied")


# Directly run the two tasks in order
number_summary()
print()
username_check()
