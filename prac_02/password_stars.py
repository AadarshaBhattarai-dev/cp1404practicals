MIN_LENGTH = 5

def main():
    """Get a valid password and print its asterisks."""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

def get_password(min_length):
    """Get a password of at least min_length characters."""
    password = input(f"Enter a password of at least {min_length} characters: ")
    while len(password) < min_length:
        print("Password too short!")
        password = input(f"Enter a password of at least {min_length} characters: ")
    return password

def print_asterisks(password):
    """Print asterisks as long as the password."""
    print("*" * len(password))


main()
