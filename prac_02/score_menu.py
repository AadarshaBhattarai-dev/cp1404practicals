def main():
    """Run the score menu program."""
    score = get_valid_score()
    choice = display_menu()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        choice = display_menu()
    print("Farewell!")

def display_menu():
    """Display menu and get user choice."""
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    choice = input(">>> ").upper()
    return choice

def get_valid_score():
    """Get valid score (0–100 inclusive)."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score

def determine_result(score):
    """Determine result from score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """Print as many stars as the score."""
    print("*" * int(score))

main()
