"""
CP1404 Practical 05
"""

def main():
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm == "n" or confirm == "no":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name

main()
