"""
CP1404/CP5632 Practical 04
"""
import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    try:
        how_many = int(input("How many quick picks? "))
    except ValueError:
        print("Please enter an integer.")
        return

    for _ in range(how_many):
        pick = generate_one_pick()
        print(" ".join(f"{n:2d}" for n in pick))

def generate_one_pick():
    pick = []
    attempts = 0
    for _ in range(100):
        if len(pick) == NUMBERS_PER_PICK:
            break
        candidate = random.randint(MIN_NUMBER, MAX_NUMBER)
        if candidate not in pick:
            pick.append(candidate)
    pick.sort()
    return pick

main()
