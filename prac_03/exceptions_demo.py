"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
-> ValueError will occur when a non-integer is entered.

2. When will a ZeroDivisionError occur?
-> ZeroDivisionError will occur  when denominator is 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
-> To avoid ZeroDivisionError we check that denominator is not zero before dividing.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
