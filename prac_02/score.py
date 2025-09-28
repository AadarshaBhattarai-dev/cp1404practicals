"""
CP1404/CP5632 - Practical
Program to determine score status (refactored with function)
"""
import random

def determine_result(score):
    """Return the result string based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    print(determine_result(score))

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} - {determine_result(random_score)}")

main()
