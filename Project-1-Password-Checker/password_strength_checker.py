"""
DecodeLabs Tasks — Cyber Security
Project 1: Password Strength Checker

Goal: Evaluate a password and classify it as Weak, Medium, or Strong
based on length and character variety (data validation + security logic).
"""

import string

# A small sample of common leaked passwords.
COMMON_LEAKED_PASSWORDS = {
    "123456", "password", "123456789", "qwerty", "abc123",
    "password123", "111111", "12345678", "Hello123", "admin",
}


def check_length(password: str, min_length: int = 8) -> bool:
    """Return True if the password meets the minimum length requirement."""
    return len(password) >= min_length


def has_uppercase(password: str) -> bool:
    return any(char.isupper() for char in password)


def has_lowercase(password: str) -> bool:
    return any(char.islower() for char in password)


def has_digit(password: str) -> bool:
    return any(char.isdigit() for char in password)


def has_symbol(password: str) -> bool:
    return any(char in string.punctuation for char in password)


def is_commonly_leaked(password: str) -> bool:
    """ reject passwords found in common leaked password lists."""
    return password.lower() in COMMON_LEAKED_PASSWORDS


def evaluate_password(password: str) -> dict:
    """
    Run all checks on a password and return a report dict containing
    each individual check result, a numeric score, and the final verdict.
    """
    if is_commonly_leaked(password):
        return {
            "length_ok": check_length(password),
            "has_uppercase": has_uppercase(password),
            "has_lowercase": has_lowercase(password),
            "has_digit": has_digit(password),
            "has_symbol": has_symbol(password),
            "score": 0,
            "strength": "Weak (found in common leaked password list)",
        }

    checks = {
        "length_ok": check_length(password),
        "has_uppercase": has_uppercase(password),
        "has_lowercase": has_lowercase(password),
        "has_digit": has_digit(password),
        "has_symbol": has_symbol(password),
    }

    # Length is a hard gate: under 8 chars is an automatic fail.

    if not checks["length_ok"]:
        checks["score"] = 0
        checks["strength"] = "Weak (too short => minimum 8 characters)"
        return checks

    # Score = 1 point per variety check passed (max 4), plus 1 bonus
    # point for length being generous (12+ chars).
    score = sum([
        checks["has_uppercase"],
        checks["has_lowercase"],
        checks["has_digit"],
        checks["has_symbol"],
    ])
    if len(password) >= 12:
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score in (3, 4):
        strength = "Medium"
    else:
        strength = "Strong"

    checks["score"] = score
    checks["strength"] = strength
    return checks


def print_report(password: str, report: dict) -> None:
    print(f"\nPassword: {'*' * len(password)}  (length: {len(password)})")
    print("-" * 40)
    print(f"Length >= 8 chars      : {report['length_ok']}")
    print(f"Contains uppercase     : {report['has_uppercase']}")
    print(f"Contains lowercase     : {report['has_lowercase']}")
    print(f"Contains digit         : {report['has_digit']}")
    print(f"Contains symbol        : {report['has_symbol']}")
    print(f"Score                  : {report['score']}")
    print(f"Strength               : {report['strength']}")
    print("-" * 40)


def main():
    print("=== Password Strength Checker ===")
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        if password.lower() == "quit":
            print("Goodbye!")
            break
        report = evaluate_password(password)
        print_report(password, report)


if __name__ == "__main__":
    main()