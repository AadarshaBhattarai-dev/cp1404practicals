"""
CP1404/CP5632 Practical 03 - Files, Exceptions
"""

finished = False
result = 0

while not finished:
    try:
        number = int(input("Enter a valid integer: "))
        result = number * 2
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"The result is {result}")
