user_name = input("Enter your name: ")

print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

menu_choice = input(">>> ").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {user_name}")
    elif menu_choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Oops! That's not a valid choice.")

    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    
menu_choice = input(">>> ").upper()
print("Finished.")