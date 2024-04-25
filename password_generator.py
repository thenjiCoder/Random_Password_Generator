# Import necessary modules
import random
import string

# Define a function to generate a password
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type should be selected.")

    return ''.join(random.choice(characters) for _ in range(length))

# Get user input for password criteria
def get_user_input():
    length = int(input("Enter the length of the password: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    return length, use_letters, use_numbers, use_symbols

# Main function to generate password based on user input
def main():
    length, use_letters, use_numbers, use_symbols = get_user_input()
    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("Generated Password:", password)
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
