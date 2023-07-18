def encrypt(message, shift):
    encrypted_message = ""
    for letter in message:
        if letter.isalpha():
            ascii_offset = ord('A') if letter.isupper() else ord('a')
            encrypted_letter = chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_letter
        else:
            encrypted_message += letter
    return encrypted_message


def decrypt(message, shift):
    return encrypt(message, -shift)


def main():
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ")
    if choice.upper() == 'E':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice.upper() == 'D':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")


if __name__ == "__main__":
    main()
