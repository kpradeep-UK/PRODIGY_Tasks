import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @!#$%^&*()_+=-]", password) is None

    errors = {
        'Length Error': length_error,
        'Digit Error': digit_error,
        'Uppercase Error': uppercase_error,
        'Lowercase Error': lowercase_error,
        'Symbol Error': symbol_error,
    }

    password_strength = "Strong" if not any(errors.values()) else "Weak"

    return password_strength, errors

if __name__ == "__main__":
    password = input("Enter the password to check: ")
    strength, errors = check_password_strength(password)
    print(f"Password Strength: {strength}")
    for error, value in errors.items():
        if value:
            print(f"{error} detected")
