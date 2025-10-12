"""
CP1404/CP5632
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# first letters of each name
first_initials = [name[0] for name in names]
print("First initials:", first_initials)

# initials of full names
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print("Full initials:", full_initials)

# names that start with 'A'
a_names = [name for name in names if name.startswith('A')]
print("Names starting with A:", a_names)

# all names in alphabetical order as a single string
print("Sorted names:", " ".join(sorted(names)))

# lowercase versions of full names
lowercase_full_names = [name.lower() for name in full_names]
print("Lowercase full names:", lowercase_full_names)

# convert strings to integers
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(x) for x in almost_numbers]
print("Numbers:", numbers)

# numbers greater than 9
numbers_over_9 = [n for n in numbers if n > 9]
print("Numbers greater than 9:", numbers_over_9)

# last names of full names longer than 11 characters
long_last_names = ", ".join([name.split()[1] for name in full_names if len(name) > 11])
print("Last names of long full names:", long_last_names)
