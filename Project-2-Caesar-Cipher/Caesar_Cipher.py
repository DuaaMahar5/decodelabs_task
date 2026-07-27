"""
Project 2: Basic Encryption & Decryption (Caesar Cipher)

Goal: Encrypt user text using a shift-based (Caesar cipher) technique,
then decrypt it back to the original plaintext.
"""

ALPHABET_SIZE = 26


def encrypt(text: str, shift: int) -> str:
    """
    Encrypt text using a Caesar cipher shift.
    Wraps around at the end of the alphabet, and leaves
    spaces, numbers, and symbols untouched..
    """
    res = []
    for char in text:
        if char.isupper():
            # 'A' = 65 in ASCII, so we shift down to a 0-25 range first
            shifted = (ord(char) - ord('A') + shift) % ALPHABET_SIZE
            res.append(chr(shifted + ord('A')))
        elif char.islower():
            # 'a' = 97 in ASCII, same logic but with lowercase base
            shifted = (ord(char) - ord('a') + shift) % ALPHABET_SIZE
            res.append(chr(shifted + ord('a')))
        else:
            # Leave spaces, numbers, and punctuation untouched
            res.append(char)
    return "".join(res)


def decrypt(text: str, shift: int) -> str:
    """
    Reverses the encryption by shifting back the other way.
    Same key, opposite direction — that's why it works.
    """
    return encrypt(text, -shift)


def main():
    print("=== Caesar Cipher: Encryption & Decryption ===")

    message = input("\nEnter the text you want to encrypt: ")

    while True:
        shift_input = input("Enter a shift key (whole number, e.g. 3): ")
        try:
            shift = int(shift_input)
            break
        except ValueError:
            print("Please enter a valid whole number for the shift key.")

    encrypted_text = encrypt(message, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print("\n--- Result ---")
    print(f"Original text  : {message}")
    print(f"Shift key      : {shift}")
    print(f"Encrypted text : {encrypted_text}")
    print(f"Decrypted text : {decrypted_text}")

    if decrypted_text == message:
        print("\nVerification: decrypted text matches the original. Success!")
    else:
        print("\nVerification: mismatch detected => check the logic.")


if __name__ == "__main__":
    main()