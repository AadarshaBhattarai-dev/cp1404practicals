"""
CP1404/CP5632 Practical 04
"""
numbers = [3, 1, 4, 1, 5, 9, 2]

# 1. Change the first element of numbers to "ten" (string)
numbers[0] = "ten"

# 2. Change the last element of numbers to 1
numbers[-1] = 1

# 3. Print all the elements from numbers except the first two (slice)
print("Elements except first two:", numbers[2:])

# 4. Print whether 9 is an element of numbers
print("Is 9 in numbers?", 9 in numbers)

# Print the final list so you can visually inspect changes
print("Final numbers list:", numbers)