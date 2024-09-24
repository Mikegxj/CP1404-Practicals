MINIMUM = 4

def main():
    """Get a password of valid length and print asterisks"""
    password = input(f"Please enter a password at lease {MINIMUM} characters: ")
    while len(password) < MINIMUM:
        print("Invalid password")
        password = input(f"Please enter a password at lease {MINIMUM} characters: ")
    print('*' * len(password))

main()





