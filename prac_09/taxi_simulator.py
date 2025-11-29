"""
CP1404/CP5632 Practical
Taxi simulator program
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    print("Taxis available:")
    for i, t in enumerate(taxis):
        print(f"{i} - {t}")

def choose_taxi(taxis):
    """Prompt user to choose a taxi index; returns taxi or None if invalid."""
    try:
        index = int(input("Choose taxi: "))
    except ValueError:
        print("Invalid value; please enter a number.")
        return None
    if index < 0 or index >= len(taxis):
        print("Invalid taxi choice")
        return None
    return taxis[index]

def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    bill = 0.0
    menu_choice = ""

    print("Let's drive!")

    while menu_choice.lower() != "q":
        print("q)uit, c)hoose taxi, d)rive")
        print(f"Bill to date: ${bill:.2f}")
        menu_choice = input(">>> ").strip().lower()

        if menu_choice == "c":
            display_taxis(taxis)
            chosen = choose_taxi(taxis)
            if chosen is not None:
                current_taxi = chosen

        elif menu_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                except ValueError:
                    print("Invalid distance")
                    continue
                current_taxi.start_fare()
                driven = current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                bill += fare

        elif menu_choice == "q":
            break

        else:
            print("Invalid option")

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == "__main__":
    main()
