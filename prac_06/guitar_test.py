"""CP1404 Practical 06"""

from prac_06.guitar import Guitar


def main():
    """Test Guitar methods."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500)

    print(f"{guitar1.name} get_age() - Expected 103. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 12. Got {guitar2.get_age()}")
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

main()
