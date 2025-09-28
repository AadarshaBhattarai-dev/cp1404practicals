for i in range(1, 21, 2):
    print(i, end=' ')
print()

print("Count in 10s from 0 to 100:")
for number in range(0, 101, 10):
    print(number, end=' ')
print()

print("Count down from 20 to 1:")
for number in range(20, 0, -1):
    print(number, end=' ')
print()
number_of_stars = int(input("Number of stars: "))
for star in range(number_of_stars):
    print('*', end='')
print()
number_of_lines = int(input("Number of lines: "))
for line_number in range(1, number_of_lines + 1):
    print('*' * line_number)