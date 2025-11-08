def is_strong_password(password: str) -> bool:
    """
    Returns True if the password meets the following criteria:
    - At least 8 characters
    - Contains at least one digit
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    """

    at_least_8_char = len(password) >= 8
    contains_at_least_one_digit = any(char.isdigit() for char in password)
    contains_at_least_one_uppercase_letter = any(char.isupper() for char in password)
    contains_at_least_one_lowercase_letter = any(char.islower() for char in password)

    return (
            at_least_8_char
            and contains_at_least_one_digit
            and contains_at_least_one_uppercase_letter
            and contains_at_least_one_lowercase_letter
    )


test_passwords = {
    "Short7": False,  # Too short
    "longbutnocaps123": False,  # No uppercase
    "LONGBUTNOLOWER123": False,  # No lowercase
    "NoDigitsHere!": False,  # No digits
    "Valid123Password": True,  # Valid
    "12345678": False,  # No letters
    "lowerUPPER123": True,  # Valid
    "Mix3dCaseWithSymbols!": True,  # Valid (symbols allowed but not required)
    "UPPERlower": False,  # No digit
    "": False,  # Empty string
}

for pwd, expected in test_passwords.items():
    result = is_strong_password(pwd)
    print(f"{pwd!r:25} -> {result} (Expected: {expected})")
