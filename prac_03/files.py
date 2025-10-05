"""
CP1404/CP5632 Practical 03 - Files, Exceptions
"""

# 1. Writes name to file
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Reads name from file and greet
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3. Reads first two numbers and add
with open("numbers.txt", "r") as in_file:
    num1 = int(in_file.readline())
    num2 = int(in_file.readline())
    print(num1 + num2)

# 4. Calculates total of all numbers
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)
