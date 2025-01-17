import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """
    Generates a random password based on user-specified criteria.

    Parameters:
    - length (int): Length of the password.
    - use_uppercase (bool): Include uppercase letters.
    - use_digits (bool): Include digits.
    - use_symbols (bool): Include symbols.

    Returns:
    - str: A randomly generated password.
    """
    if length < 4:  # Minimum length check
        raise ValueError("Password length should be at least 4 characters.")

    character_pool = string.ascii_lowercase  # Start with lowercase letters

    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    # Ensure password contains at least one of each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    password.append(random.choice(string.ascii_lowercase))

    # Fill the rest of the password length with random choices
    remaining_length = length - len(password)
    password.extend(random.choices(character_pool, k=remaining_length))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print("Random Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        use_uppercase = input("Include uppercase letters? (Y/N): ").strip().lower() == 'Y'
        use_digits = input("Include digits? (Y/N): ").strip().lower() == 'Y'
        use_symbols = input("Include symbols? (Y/N): ").strip().lower() == 'Y'

        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
