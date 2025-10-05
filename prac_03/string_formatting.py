"""
CP1404/CP5632 Practical 03 - Files, Exceptions
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9999

# Display formatted output
print(f"{year} {name} for about ${cost:,.0f}!")

# Display powers of 2, right-aligned
for exponent in range(11):
    print(f"2 ^ {exponent:2} is {2 ** exponent:4}")
